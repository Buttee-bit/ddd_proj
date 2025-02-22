from faststream import FastStream
from faststream.kafka import KafkaBroker
from dishka.integrations.faststream import FastStreamProvider, FromDishka, setup_dishka

broker = KafkaBroker("localhost:9092")

app = FastStream(broker)


@broker.subscriber("test")
async def base_handler(body):
    print(body)


# setup_dishka(app=app, provider=FastStreamProvider)
