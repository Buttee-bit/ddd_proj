from functools import lru_cache
import logging
from motor.motor_asyncio import AsyncIOMotorClient
from motor.core import AgnosticClient

from punq import (
    Container,
    Scope,
)

from backend.aplications.parser_tg.infra.repositoryes.base import BaseChannelRepository, BaseNewsRepository
from backend.aplications.parser_tg.infra.repositoryes.channels_repo import ChannelsRepository
from backend.aplications.parser_tg.infra.repositoryes.news_repo import NewsRepository
from backend.aplications.parser_tg.logic.commands.news import CreateNewsCommandHandler
from backend.aplications.parser_tg.logic.commands.channels import CreateChannelCommandHandler, CreateChannelsCommand
from backend.aplications.parser_tg.logic.mediator.base import Mediator
from backend.aplications.parser_tg.logic.queries.channels import GetChannelsQuery, GetChannelQueryHandler
from backend.aplications.parser_tg.setings.setting import Settings



@lru_cache(1)
def init_conatainer() -> Container:
    return _init_container()

def _init_container() -> Container:
    container = Container()

    container.register(Settings, instance=Settings(), scope=Scope.singleton)

    settings: Settings = container.resolve(Settings)

    def create_mongodb_client():
        return AsyncIOMotorClient(
            settings.mongodb_connection_uri,
            serverSelectionTimeoutMS=3000,
        )

    container.register(AsyncIOMotorClient, factory=create_mongodb_client, scope=Scope.singleton)
    client = container.resolve(AsyncIOMotorClient)

    def init_news_repository() -> BaseNewsRepository:
        return NewsRepository(
            mongo_db_client=client,
            mongo_db_db_name=settings.mongodb_news_database_name,
            mongo_db_collection_name=settings.mongodb_news_collection_name
        )

    container.register(BaseNewsRepository, factory=init_news_repository, scope=Scope.singleton)


    def init_channels_repository() -> BaseChannelRepository:
        return ChannelsRepository(
            mongo_db_client=client,
            mongo_db_db_name=settings.mongodb_channels_database_name,
            mongo_db_collection_name=settings.mongodb_channels_collection_name
        )

    container.register(BaseChannelRepository, factory=init_channels_repository, scope=Scope.singleton)


    container.register(GetChannelQueryHandler)


    def init_mediator() -> Mediator:
        mediator = Mediator()


        # Commands
        create_channel_handler = CreateChannelCommandHandler(
            _mediator=mediator,
            channels_repository=container.resolve(BaseChannelRepository)
        )

        mediator.register_command(
            CreateChannelsCommand,
            [create_channel_handler]
        )

        # Queries
        mediator.register_query(
            GetChannelsQuery,
            container.resolve(GetChannelQueryHandler)
        )


        return mediator

    container.register(Mediator, factory=init_mediator)

    return container