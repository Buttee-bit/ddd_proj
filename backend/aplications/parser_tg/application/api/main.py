from contextlib import asynccontextmanager
from fastapi import FastAPI
from punq import Container
from backend.aplications.parser_tg.logic.init import init_conatainer
from backend.aplications.parser_tg.application.api.handlers.channels import router as channel_router



@asynccontextmanager
async def lifespan(app: FastAPI):
    container: Container = init_conatainer()
    yield

def create_app() -> FastAPI:
    app = FastAPI(
        title="API Application Docker !!!!",
        version="0.0.1",
        contact={"name": "Punq", "email": "g8nYK@example.com"},
        debug=True,
        lifespan=lifespan,
    )
    app.include_router(channel_router)

    return app