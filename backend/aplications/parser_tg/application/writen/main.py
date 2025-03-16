from punq import Container

from faststream import FastStream, Logger, Depends
from faststream.kafka import KafkaBroker
from backend.aplications.parser_tg.application.scrapping.tg import MessageDTO
from backend.aplications.parser_tg.logic.commands.news import CreateNewsCommand
from backend.aplications.parser_tg.logic.init import init_conatainer
from backend.aplications.parser_tg.logic.mediator.base import Mediator

def main() -> FastStream:
    broker = KafkaBroker(bootstrap_servers=["kafka:29092"])
    app = FastStream(broker=broker)
    container = init_conatainer()

    @broker.subscriber("telegram_messages")
    @broker.publisher("recive_news")
    async def handle_telegram_message(
        data: MessageDTO,
        logger: Logger,
        mediator: Mediator = Depends(lambda: container.resolve(Mediator)),
    ):
        logger.warning(f"Получено сообщение из Kafka: {data}")
        await mediator.handle_command(
            CreateNewsCommand(
                text=data.message,
                title=data.message[:50],
                published_at=data.time_publish,
                oid_channel=data.chat_oid
            )
        )

    return app