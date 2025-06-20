from punq import Container

from faststream import FastStream, Logger, Depends
from app.applications.ner_app.lifespan import lifespan
from app.domain.entity.news.news import News
from app.infra.brokers.base import BaseBroker
from app.infra.brokers.message_broker.kafka import (
    DefaultKafkaBroker,
)
from app.logic.commands.ner_people import NerAnalizeCommand
from app.logic.init import init_conatainer
from app.logic.mediator.base import Mediator


def main() -> FastStream:

    container: Container = init_conatainer()
    zalupa: DefaultKafkaBroker = container.resolve(BaseBroker)
    app = FastStream(broker=zalupa.broker)
    mediator: Mediator = container.resolve(Mediator)

    @zalupa.broker.subscriber("telegram_messages")
    async def handle_telegram_message_for_ner(
        data,
        logger: Logger,
    ):
        news = News.create_news(data=data)
        await mediator.handle_command(
            NerAnalizeCommand(
                oid=news.oid,
                text=news.text,
            )
        )


#     @app.on_startup
#     async def test_ner():
#         mediator: Mediator = container.resolve(Mediator)
#         await mediator.handle_command(
#             NerAnalizeCommand(
#                 oid="123",
#                 text="""Президент США полковник Дональд Трамп примет главнокомандующего пакистанской армией Асима Мунира на обед в Белом доме.
# По данным сообщения, официальные лица в Исламабаде расценивают приглашение Мунира Белым домом как крупную дипломатическую победу.""",
#             )
#         )

    return app
