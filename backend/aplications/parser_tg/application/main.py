from faststream import FastStream
from faststream.kafka import KafkaBroker
from dishka.integrations.faststream import FastStreamProvider, FromDishka, setup_dishka
from backend.aplications.parser_tg.ioc import container

broker = KafkaBroker()
app = FastStream(broker)


@broker.subscriber("test-topic")
async def handle():
    await broker.publish("Hi!", topic="another-topic")

@app.after_startup
async def test():
    await broker.publish("", topic="test-topic")


# setup_dishka(app=app, container=container, auto_inject=True)