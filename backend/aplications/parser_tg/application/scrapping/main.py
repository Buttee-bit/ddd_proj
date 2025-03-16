from punq import Container

from faststream import FastStream, Logger, Depends
from faststream.kafka import KafkaBroker

from backend.aplications.parser_tg.application.scrapping.dto import ChannelDTO, ListChannelDTO
from backend.aplications.parser_tg.application.scrapping.tg import MessageDTO, TgParsServices
from backend.aplications.parser_tg.logic.init import init_conatainer
from backend.aplications.parser_tg.logic.mediator.base import Mediator
from backend.aplications.parser_tg.logic.queries.channels import GetChannelsQuery


def main() -> FastStream:
    broker = KafkaBroker(bootstrap_servers=["kafka:29092"])
    app = FastStream(broker=broker)


    @app.after_startup
    async def start_telegram_listener(
        logger: Logger,
        container: Container = Depends(init_conatainer),
    ):
        mediator: Mediator = container.resolve(Mediator)
        tg_services: TgParsServices = container.resolve(TgParsServices)
        channels = await mediator.handle_query(GetChannelsQuery())
        channelsDTO = ListChannelDTO(channels=[ChannelDTO(oid=chat.oid, url=chat.url) for chat in channels])
        logger.warning(f"Начато прослушивание !")
        await tg_services.start_listening(channels=channelsDTO)

    return app