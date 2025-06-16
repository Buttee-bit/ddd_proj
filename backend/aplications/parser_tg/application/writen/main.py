from punq import Container

from faststream import FastStream, Logger, Depends
from faststream.kafka import KafkaBroker
from backend.aplications.parser_tg.domain.entity.news.news import News
from backend.aplications.parser_tg.logic.commands.news import CreateNewsCommand
from backend.aplications.parser_tg.logic.init import init_conatainer
from backend.aplications.parser_tg.logic.mediator.base import Mediator
from backend.aplications.parser_tg.setings.setting import Setings

def main() -> FastStream:
    container = init_conatainer()
    setting: Setings = container.resolve(Setings)
    broker = KafkaBroker(bootstrap_servers=setting.kafka_url)
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
        await broker.publish(
            topic="Recive_messsages",
            message=data
        )
    return app