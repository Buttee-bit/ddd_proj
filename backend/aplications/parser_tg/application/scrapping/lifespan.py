from contextlib import asynccontextmanager
from faststream import ContextRepo
from punq import Container
from backend.aplications.parser_tg.infra.brokers.base import BaseBroker
from backend.aplications.parser_tg.infra.brokers.message_broker.kafka import NewsKafkaBroker
from backend.aplications.parser_tg.logic.init import init_conatainer


@asynccontextmanager
async def lifespan(context: ContextRepo):
    container: Container = init_conatainer()
    broker: NewsKafkaBroker = container.resolve(BaseBroker)
    await broker.start()
    
    yield
    await broker.stop()
