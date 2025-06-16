import asyncio
from punq import Container
from faststream import FastStream, Logger
from backend.aplications.parser_tg.infra.telegram.tg import (
    TgParsServices,
)
from backend.aplications.parser_tg.infra.brokers.base import BaseBroker
from backend.aplications.parser_tg.infra.brokers.message_broker.kafka import (
    NewsKafkaBroker,
)

from backend.aplications.parser_tg.logic.commands.channels import (
    SubscribeChannelCommand,
)
from backend.aplications.parser_tg.logic.init import init_conatainer
from backend.aplications.parser_tg.logic.mediator.base import Mediator
from backend.aplications.parser_tg.application.scrapping.lifespan import lifespan
from backend.aplications.parser_tg.domain.events.channels import NewChannelReceivedEvent


async def run_telegram_listener(logger: Logger, tg_services: TgParsServices):
    try:
        await tg_services.tg_client.connect()
        await tg_services.start_listening()
    except Exception as e:
        logger.error(f"Ошибка в Telegram listener: {e}")
        raise


def main() -> FastStream:
    container: Container = init_conatainer()
    news_broker: NewsKafkaBroker = container.resolve(BaseBroker)
    tg_services: TgParsServices = container.resolve(TgParsServices)

    app = FastStream(lifespan=lifespan, broker=news_broker.broker)

    @app.after_startup
    async def on_startup(logger: Logger):
        telegram_task = asyncio.create_task(run_telegram_listener(logger, tg_services))

    @news_broker.broker.subscriber("update-channels-telegramm")
    async def hasndle_update_channels(msg: NewChannelReceivedEvent, logger: Logger):
        container: Container = init_conatainer()
        mediator: Mediator = container.resolve(Mediator)
        try:
            await mediator.handle_command(SubscribeChannelCommand(url=msg.link_channel))
        except Exception as exception:
            logger.warning(f"exception: {exception}")

    return app
