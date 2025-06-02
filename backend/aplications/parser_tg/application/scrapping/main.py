import asyncio
from punq import Container
from faststream import FastStream, Logger, Depends
from backend.aplications.parser_tg.application.scrapping.dto import (
    ChannelDTO,
    ListChannelDTO,
)
from backend.aplications.parser_tg.application.scrapping.tg import (
    TgParsServices,
)
from backend.aplications.parser_tg.infra.brokers.base import BaseBroker
from backend.aplications.parser_tg.infra.brokers.message_broker.kafka import NewsKafkaBroker

from backend.aplications.parser_tg.logic.init import init_conatainer
from backend.aplications.parser_tg.logic.mediator.base import Mediator
from backend.aplications.parser_tg.logic.queries.channels import GetChannelsQuery
from backend.aplications.parser_tg.application.scrapping.lifespan import lifespan


async def run_telegram_listener(
    logger: Logger,
    container: Container,
    tg_services: TgParsServices
):
    try:
        await tg_services.tg_client.connect()
        mediator: Mediator = container.resolve(Mediator)
        channels = await mediator.handle_query(GetChannelsQuery())
        channelsDTO = ListChannelDTO(
            channels=[ChannelDTO(oid=chat.oid, url=chat.url) for chat in channels]
        )
        logger.warning(f"Начато прослушивание Telegram!")
        await tg_services.start_listening(channels=channelsDTO)
    except Exception as e:
        logger.error(f"Ошибка в Telegram listener: {e}")
        raise


def main() -> FastStream:
    container: Container = init_conatainer()
    news_broker: NewsKafkaBroker = container.resolve(BaseBroker)
    tg_services: TgParsServices = container.resolve(TgParsServices)
    app = FastStream(
        lifespan=lifespan,
        broker=news_broker.broker
    )

    @app.after_startup
    async def on_startup(logger: Logger):
        telegram_task = asyncio.create_task(
            run_telegram_listener(logger, container, tg_services)
        )

    @news_broker.broker.subscriber("update-channels")
    async def hasndle_update_channels(logger: Logger):
        ...

    return app