from contextlib import asynccontextmanager
from fastapi import FastAPI
from punq import Container
from faststream.kafka import KafkaBroker



from backend.aplications.parser_tg.application.api.lifespan import lifespan
from backend.aplications.parser_tg.application.api.handlers.channels import router as channel_router
from backend.aplications.parser_tg.application.api.handlers.entity import router as entity_router
from backend.aplications.parser_tg.application.api.handlers.news import router as news_router




def create_app() -> FastAPI:
    app = FastAPI(
        title="API Application Docker ",
        version="0.0.1",
        contact={"name": "Punq", "email": "g8nYK@example.com"},
        debug=True,
        lifespan=lifespan,
    )
    app.include_router(channel_router)
    app.include_router(entity_router)
    app.include_router(news_router)
    return app