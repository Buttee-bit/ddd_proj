from punq import Container
import logging
from faststream import FastStream, Logger, Depends
from faststream.kafka import KafkaBroker
from app.domain.entity.news.news import News
from app.logic.commands.news import CreateNewsCommand
from app.logic.init import init_conatainer
from app.logic.mediator.base import Mediator
from app.settings.setting import Setings


def main() -> FastStream:
    container = init_conatainer()
    setting: Setings = container.resolve(Setings)
    broker = KafkaBroker(bootstrap_servers=setting.kafka_url)
    app = FastStream(broker=broker)
    mediator: Mediator = container.resolve(Mediator)

    @broker.subscriber("telegram_messages")
    async def handle_telegram_message(data):
        news = News.create_news(data=data)
        await mediator.handle_command(CreateNewsCommand(news=news))

    return app
