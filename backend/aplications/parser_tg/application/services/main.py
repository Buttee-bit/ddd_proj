from punq import Container

from faststream import FastStream, Logger, Depends
from faststream.kafka import KafkaBroker
from backend.aplications.parser_tg.application.services.dto import ChannelDTO, ListChannelDTO
from backend.aplications.parser_tg.application.services.tg import MessageDTO, TgParsServices
from backend.aplications.parser_tg.logic.init import init_conatainer
from backend.aplications.parser_tg.logic.mediator.base import Mediator
from backend.aplications.parser_tg.logic.queries.channels import GetChannelsQuery


broker = KafkaBroker()
app = FastStream(broker=broker)

@app.after_startup
async def start_telegram_listener(
    container: Container = Depends(init_conatainer),
):
    mediator: Mediator = container.resolve(Mediator)
    tg_services: TgParsServices = container.resolve(TgParsServices)
    channels = await mediator.handle_query(GetChannelsQuery())
    channelsDTO = ListChannelDTO(channels=[ChannelDTO(oid=chat.oid, url=chat.url) for chat in channels])
    await tg_services.start_listening(channels=channelsDTO)


@broker.subscriber("telegram_messages")
async def handle_telegram_message(data:MessageDTO, logger: Logger):
    logger.warning(f"Получено сообщение из Kafka: {data}")
