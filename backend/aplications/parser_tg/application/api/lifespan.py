
from contextlib import asynccontextmanager
from fastapi import FastAPI
from punq import Container
from backend.aplications.parser_tg.infra.brokers.base import BaseBroker
from backend.aplications.parser_tg.logic.init import init_conatainer


@asynccontextmanager
async def lifespan(app: FastAPI):
    container: Container = init_conatainer()
    broker: BaseBroker = container.resolve(BaseBroker)
    await broker.start()
    yield
    await broker.stop()