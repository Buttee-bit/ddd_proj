import asyncio
from punq import Container
from faststream import FastStream, Logger
from app.infra.telegram.tg import (
    TgParsServices,
)
from app.infra.brokers.base import BaseBroker
from app.infra.brokers.message_broker.kafka import (
    DefaultKafkaBroker,
)

from app.logic.commands.channels import (
    SubscribeChannelCommand,
)
from app.logic.init import init_conatainer
from app.logic.mediator.base import Mediator
from applications.scrapping.lifespan import lifespan
from app.domain.events.channels import NewChannelReceivedEvent


async def run_telegram_listener(logger: Logger, tg_services: TgParsServices):
    try:
        await tg_services.tg_client.connect()
        await tg_services.start_listening()
    except Exception as e:
        logger.error(f"Ошибка в Telegram listener: {e}")
        raise e


def main() -> FastStream:
    container: Container = init_conatainer()
    news_broker: DefaultKafkaBroker = container.resolve(BaseBroker)
    tg_services: TgParsServices = container.resolve(TgParsServices)

    app = FastStream(lifespan=lifespan, broker=news_broker.broker)

    @after_startup
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
