from punq import Container

from faststream import FastStream, Logger, Depends
from faststream.kafka import KafkaBroker
from backend.aplications.parser_tg.domain.entity.news.news import News
from backend.aplications.parser_tg.logic.commands.ner_people import AddNerPeopleToDocumentCommand, FindPeopleCommand
from backend.aplications.parser_tg.logic.init import init_conatainer
from backend.aplications.parser_tg.logic.mediator.base import Mediator

def main() -> FastStream:
    broker = KafkaBroker(bootstrap_servers=["kafka:29092"])
    app = FastStream(broker=broker)
    container = init_conatainer()

    @broker.subscriber("Recive_messsages")
    async def handle_telegram_message(
        data: News,
        logger: Logger,
        mediator: Mediator = Depends(lambda: container.resolve(Mediator)),
    ):

        logger.warning(f"Получено сообщение из Kafka: {data}")
        await mediator.handle_command(
            FindPeopleCommand(
                oid=data.oid,
                text=data.text,
            )
        )

    return app