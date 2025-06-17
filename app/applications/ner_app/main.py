from punq import Container

from faststream import FastStream, Logger, Depends
from applications.ner_app.lifespan import lifespan
from app.domain.entity.news.news import News
from app.infra.brokers.base import BaseBroker
from app.infra.brokers.message_broker.kafka import (
    DefaultKafkaBroker,
)
from app.logic.commands.ner_people import NerAnalizeCommand
from app.logic.init import init_conatainer
from app.logic.mediator.base import Mediator
from setings.setting import Setings


def main() -> FastStream:
    container: Container = init_conatainer()
    broker: DefaultKafkaBroker = container.resolve(BaseBroker)
    app = FastStream(broker=broker.broker, lifespan=lifespan)

    @broker.broker.subscriber("telegram_messages")
    async def handle_telegram_message(
        data: News,
        logger: Logger,
        mediator: Mediator = Depends(lambda: container.resolve(Mediator)),
    ):
        await mediator.handle_command(
            NerAnalizeCommand(
                oid=data.oid,
                text=data.text,
            )
        )

    @app.on_startup
    async def test_ner():
        mediator: Mediator = container.resolve(Mediator)
        await mediator.handle_command(
            NerAnalizeCommand(
                oid="123",
                text="Полтавщина:\n5х БпЛА у Кременчуцькому районі.\n7х БпЛА у Полтавському район, втч повз Полтаву.\n\nДніпропетровщина:\n12х одинарних БпЛА через область у напрямку Криворізького району.\n\nМиколаївщина:\n8х БпЛА з Херсонщини у напрямку Баштанського району області.",
            )
        )

    return app
