from contextlib import asynccontextmanager
from faststream import ContextRepo
from punq import Container
from app.infra.brokers.base import BaseBroker
from app.infra.brokers.message_broker.kafka import DefaultKafkaBroker
from app.logic.init import init_conatainer


@asynccontextmanager
async def lifespan(context: ContextRepo):
    container: Container = init_conatainer()
    broker: DefaultKafkaBroker = container.resolve(BaseBroker)
    await broker.start()
    yield
    await broker.stop()
