import logging
from faststream import FastStream, Logger, Depends
from faststream.kafka import KafkaBroker
from dishka.integrations.faststream import FastStreamProvider, FromDishka, setup_dishka, inject
from backend.aplications.parser_tg.application.handlers.news import router as news_router
from backend.aplications.parser_tg.ioc import _init_container
from backend.aplications.parser_tg.setings.setting import ParserTgSettings
from punq import Container

broker = KafkaBroker()
broker.include_router(news_router)
app = FastStream(broker=broker)

@broker.subscriber("test-topic")
async def handle():
    await broker.publish("Hi!", topic="another-topic")

@app.after_startup
@inject
async def test(
    logger: Logger,
    container: Container = Depends(_init_container),
):
    settings = container.resolve(ParserTgSettings)
    logger.info(f"settings: {settings}")
    ...