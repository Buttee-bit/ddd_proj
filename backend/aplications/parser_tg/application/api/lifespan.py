
from contextlib import asynccontextmanager
from fastapi import FastAPI
from faststream.kafka import KafkaBroker
from punq import Container
from backend.aplications.parser_tg.infra.brokers.message_broker.kafka import NewsKafkaBroker
from backend.aplications.parser_tg.logic.init import init_conatainer


@asynccontextmanager
async def lifespan(app: FastAPI):
    container: Container = init_conatainer()
    broker: NewsKafkaBroker = container.resolve(NewsKafkaBroker)
    await broker.start()
    yield
    # await broker.close()