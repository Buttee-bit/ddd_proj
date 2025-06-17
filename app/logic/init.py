from functools import lru_cache
import logging
from motor.motor_asyncio import AsyncIOMotorClient
from punq import (
    Container,
    Scope,
)
from telethon import TelegramClient
from app.infra.analizer.pullenti_analizer import PullentiAnalizer
from app.infra.telegram.tg import TgParsServices

from app.infra.brokers.base import BaseBroker
from app.infra.brokers.message_broker.kafka import (
    DefaultKafkaBroker,
)
from app.infra.repositoryes.base import (
        BaseNerPeopleRepository,
    BaseNewsRepository,
)
from app.infra.repositoryes.channels.base import BaseChannelRepository
from app.infra.repositoryes.channels.mongo_channels import ChannelsRepository
from app.infra.repositoryes.ners.peoples import (
    NerPeoplesRepository,
    NerPeoplesUniqueRepository,
)
from app.infra.repositoryes.news_repo import NewsRepository
from app.logic.commands.ner_people import (
    AddNerPeopleToDocumentCommand,
    AddNerPeopleToDocumentHandler,
    NerAnalizeCommand,
    NerAnalizeHandler,
)
from app.logic.commands.news import (
    CreateNewsCommandHandler,
    CreateNewsCommand,
)
from app.logic.commands.channels import (
    CreateChannelCommandHandler,
    CreateChannelsCommand,
    SubscribeChannelCommand,
    SubscribeChannelInfoCommandHandler,
)
from app.logic.mediator.base import Mediator
from app.logic.queries.channels import (
    GetChannelsQueryWithFilter,
    GetChannelQueryWithilterHandler,
    GetChannelQueryHandler,
    GetChannelsQuery,
)
from app.logic.queries.news import (
    GetNewslatestHandler,
    GetNewsLatestQuery,
)
from app.settings.setting import Setings
from faststream.kafka import KafkaBroker


@lru_cache(1)
def init_conatainer() -> Container:
    return _init_container()


def _init_container() -> Container:
    container = Container()
    container.register(Setings, instance=Setings(), scope=Scope.singleton)
    settings: Setings = container.resolve(Setings)
    logging.warning(f'settings: {settings}')
    def create_mongodb_client():
        return AsyncIOMotorClient(
            settings.mongodb_connection_uri,
            serverSelectionTimeoutMS=3000,
        )

    container.register(
        AsyncIOMotorClient, factory=create_mongodb_client, scope=Scope.singleton
    )
    client = container.resolve(AsyncIOMotorClient)

    def create_news_broker() -> BaseBroker:
        return DefaultKafkaBroker(broker=KafkaBroker(bootstrap_servers=settings.kafka_url))

    container.register(
        service=BaseBroker, factory=create_news_broker, scope=Scope.singleton
    )

    def _init_TgServices() -> TgParsServices:
        return TgParsServices(
            tg_client=TelegramClient(
                settings.session_file,
                settings.tg_api_id,
                settings.tg_api_hash,
                app_version="1.0.0",
                device_model="Desktop",
                system_version="4.17.30-vxCUSTOM",
            ),
            broker=container.resolve(BaseBroker),
            channels_repo=container.resolve(BaseChannelRepository)
        )

    container.register(TgParsServices, factory=_init_TgServices, scope=Scope.singleton)

    # Repositories
    def init_news_repository() -> BaseNewsRepository:
        return NewsRepository(
            mongo_db_client=client,
            mongo_db_db_name=settings.mongodb_news_database_name,
            mongo_db_collection_name=settings.mongodb_news_collection_name,
        )

    def init_channels_repository() -> BaseChannelRepository:
        return ChannelsRepository(
            mongo_db_client=client,
            mongo_db_db_name=settings.mongodb_channels_database_name,
            mongo_db_collection_name=settings.mongodb_channels_collection_name,
        )

    def init_ner_people_repository() -> BaseNerPeopleRepository:
        return NerPeoplesRepository(
            mongo_db_client=client,
            mongo_db_db_name=settings.mongodb_ner_database_name,
            mongo_db_collection_name=settings.mongodb_ner_collection_persones_name,
        )

    def init_unique_ner_repository() -> BaseNerPeopleRepository:
        return NerPeoplesUniqueRepository(
            mongo_db_client=client,
            mongo_db_db_name=settings.mongodb_ner_database_name,
            mongo_db_collection_name=settings.mongodb_ner_collection_unique_persones_name,
        )

    container.register(
        BaseNewsRepository, factory=init_news_repository, scope=Scope.singleton
    )
    container.register(
        NerPeoplesUniqueRepository,
        factory=init_unique_ner_repository,
        scope=Scope.singleton,
    )
    container.register(
        BaseChannelRepository, factory=init_channels_repository, scope=Scope.singleton
    )
    container.register(
        BaseNerPeopleRepository,
        factory=init_ner_people_repository,
        scope=Scope.singleton,
    )

    # Analizers
    def init_analizer_persones() -> PullentiAnalizer:
        return PullentiAnalizer(address_=settings.pulenty_server)

    container.register(
        PullentiAnalizer, factory=init_analizer_persones, scope=Scope.singleton
    )

    def init_mediator() -> Mediator:
        mediator = Mediator()
        # Commands
        create_channel_handler = CreateChannelCommandHandler(
            _mediator=mediator,
            channels_repository=container.resolve(BaseChannelRepository),
            tg_services=container.resolve(TgParsServices),
            broker=container.resolve(BaseBroker),
        )
        create_find_people_command = NerAnalizeHandler(
            _mediator=mediator,
            ner_people_repository=container.resolve(BaseNerPeopleRepository),
            news_repository=container.resolve(BaseNewsRepository),
            unique_ner_repository=container.resolve(NerPeoplesUniqueRepository),
            analizer=container.resolve(PullentiAnalizer),
        )
        add_ner_people_to_documenthandler = AddNerPeopleToDocumentHandler(
            _mediator=mediator,
            ner_people_repository=container.resolve(BaseNerPeopleRepository),
            news_repository=container.resolve(BaseNewsRepository),
            analizer=container.resolve(PullentiAnalizer),
        )
        create_news_handler = CreateNewsCommandHandler(
            _mediator=mediator, news_repository=container.resolve(BaseNewsRepository)
        )

        update_channel_info = SubscribeChannelInfoCommandHandler(
            _mediator=mediator,
            telegram_service=container.resolve(TgParsServices),
            channel_repo=container.resolve(BaseChannelRepository)
        )

        mediator.register_command(SubscribeChannelCommand, [update_channel_info])

        mediator.register_command(CreateNewsCommand, [create_news_handler])
        mediator.register_command(
            AddNerPeopleToDocumentCommand, [add_ner_people_to_documenthandler]
        )
        mediator.register_command(NerAnalizeCommand, [create_find_people_command])
        mediator.register_command(CreateChannelsCommand, [create_channel_handler])

        # Queries
        mediator.register_query(
            query=GetChannelsQueryWithFilter,
            query_handler=container.resolve(GetChannelQueryWithilterHandler),
        )
        mediator.register_query(
            query=GetChannelsQuery,
            query_handler=container.resolve(GetChannelQueryHandler),
        )
        mediator.register_query(
            query=GetNewsLatestQuery,
            query_handler=container.resolve(GetNewslatestHandler),
        )
        return mediator

    container.register(GetChannelQueryWithilterHandler)
    container.register(GetChannelQueryHandler)
    container.register(GetNewslatestHandler)
    container.register(Mediator, factory=init_mediator)
    return container
