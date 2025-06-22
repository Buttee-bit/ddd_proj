import logging
from punq import Container

from faststream import FastStream
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
    ):
        news = News.create_news(data=data)
        list_ner = await mediator.handle_command(
            NerAnalizeCommand(
                oid=news.oid,
                text=news.text,
            )
        )
        logging.warning(f'news:{news.oid}\nlist_ner: {list_ner}')

    return app
