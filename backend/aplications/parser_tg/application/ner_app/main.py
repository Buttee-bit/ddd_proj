from punq import Container

from faststream import FastStream, Logger, Depends
from backend.aplications.parser_tg.application.ner_app.lifespan import lifespan
from backend.aplications.parser_tg.domain.entity.news.news import News
from backend.aplications.parser_tg.infra.brokers.base import BaseBroker
from backend.aplications.parser_tg.infra.brokers.message_broker.kafka import NewsKafkaBroker
from backend.aplications.parser_tg.logic.commands.ner_people import FindPeopleCommand
from backend.aplications.parser_tg.logic.init import init_conatainer
from backend.aplications.parser_tg.logic.mediator.base import Mediator
from backend.aplications.parser_tg.setings.setting import Setings


def main() -> FastStream:
    container: Container = init_conatainer()
    broker: NewsKafkaBroker = container.resolve(BaseBroker)
    app = FastStream(broker=broker.broker, lifespan=lifespan)

    @broker.broker.subscriber("telegram_messages")
    async def handle_telegram_message(
        data: News,
        logger: Logger,
        mediator: Mediator = Depends(lambda: container.resolve(Mediator)),
    ):

        await mediator.handle_command(
            FindPeopleCommand(
                oid=data.oid,
                text=data.text,
            )
        )

    return app
