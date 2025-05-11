from contextlib import asynccontextmanager
from fastapi import FastAPI
from punq import Container
from faststream.kafka import KafkaBroker

from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

from backend.aplications.parser_tg.application.api.lifespan import lifespan
from backend.aplications.parser_tg.application.api.handlers.channels import router as channel_router
from backend.aplications.parser_tg.application.api.handlers.entity import router as entity_router
from backend.aplications.parser_tg.application.api.handlers.news import router as news_router



def configure_tracer() -> None:
    trace.set_tracer_provider(
        TracerProvider(resource=Resource.create({SERVICE_NAME: "backend_fast_api"}))
    )
    jaeger_exporter = JaegerExporter(
        collector_endpoint="http://localhost:14268/api/traces",
    )
    trace.get_tracer_provider().add_span_processor(BatchSpanProcessor(jaeger_exporter))


def create_app() -> FastAPI:
    configure_tracer()
    app = FastAPI(
        title="API Application Docker ",
        version="0.0.1",
        contact={"name": "Punq", "email": "g8nYK@example.com"},
        debug=True,
        lifespan=lifespan,
    )
    FastAPIInstrumentor.instrument_app(app)
    app.include_router(channel_router)
    app.include_router(entity_router)
    app.include_router(news_router)

    return app