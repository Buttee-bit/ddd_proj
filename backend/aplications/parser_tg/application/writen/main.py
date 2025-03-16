from punq import Container

from faststream import FastStream, Logger, Depends
from faststream.kafka import KafkaBroker
from backend.aplications.parser_tg.domain.entity.news.news import News
from backend.aplications.parser_tg.logic.commands.news import CreateNewsCommand
from backend.aplications.parser_tg.logic.init import init_conatainer
from backend.aplications.parser_tg.logic.mediator.base import Mediator

def main() -> FastStream:
    broker = KafkaBroker(bootstrap_servers=["kafka:29092"])
    app = FastStream(broker=broker)
    container = init_conatainer()

    @broker.subscriber("telegram_messages")
    async def handle_telegram_message(
        data: News,
        logger: Logger,
        mediator: Mediator = Depends(lambda: container.resolve(Mediator)),
    ):
        logger.warning(f"Получено сообщение из Kafka: {data}")
        await mediator.handle_command(
            CreateNewsCommand(
                text=data.text,
                title=data.title,
                published_at=data.published_at,
                oid_channel=data.oid_channel,
            )
        )
        logger.warning(f"Сообщение: {data} отправлено в очередь Recive_messsages")
        await broker.publish(
            topic="Recive_messsages",
            message=data
        )
    return app