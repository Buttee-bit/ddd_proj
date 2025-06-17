
from contextlib import asynccontextmanager
from fastapi import FastAPI
from punq import Container
from app.infra.telegram.tg import TgParsServices
from app.infra.brokers.base import BaseBroker
from app.logic.init import init_conatainer


@asynccontextmanager
async def lifespan(app: FastAPI):
    container: Container = init_conatainer()
    broker: BaseBroker = container.resolve(BaseBroker)
    tg_services: TgParsServices = container.resolve(TgParsServices)
    await broker.start()
    await tg_services.tg_client.connect()
    yield
    await broker.stop()
    await tg_services.tg_client.disconnect()
