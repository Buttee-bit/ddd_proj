from punq import Container

from faststream import FastStream, Logger, Depends
from faststream.kafka import KafkaBroker
from app.domain.entity.news.news import News
from app.logic.commands.news import CreateNewsCommand
from app.logic.init import init_conatainer
from app.logic.mediator.base import Mediator
from setings.setting import Setings

def main() -> FastStream:
    container = init_conatainer()
    setting: Setings = container.resolve(Setings)
    broker = KafkaBroker(bootstrap_servers='kafka:9092')
    app = FastStream(broker=broker)

    @broker.subscriber("telegram_messages")
    async def handle_telegram_message(
        data: News,
        logger: Logger,
        mediator: Mediator = Depends(lambda: container.resolve(Mediator)),
    ):
        await mediator.handle_command(
            CreateNewsCommand(
                text=data.text,
                title=data.title,
                published_at=data.published_at,
                oid_channel=data.id_channel,
            )
        )
    return app