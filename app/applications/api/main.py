from fastapi import FastAPI


from app.applications.api.lifespan import lifespan
from app.applications.api.handlers.channels.channels import router as channel_router
from app.applications.api.handlers.entity import router as entity_router
from app.applications.api.handlers.news import router as news_router
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173",
]


def create_app() -> FastAPI:
    app = FastAPI(
        title="API Application Docker ",
        version="0.0.1",
        contact={"name": "Punq", "email": "g8nYK@example.com"},
        debug=True,
        lifespan=lifespan,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(channel_router)
    app.include_router(entity_router)
    app.include_router(news_router)
    return app
