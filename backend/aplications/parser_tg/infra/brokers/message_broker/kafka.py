import logging
import orjson
from dataclasses import dataclass
from typing import AsyncIterable
from aiokafka import AIOKafkaConsumer,AIOKafkaProducer
from backend.aplications.parser_tg.infra.brokers.base import BaseBroker

@dataclass
class NewsKafkaBroker(BaseBroker):
    consumer: AIOKafkaConsumer
    produser: AIOKafkaProducer

    async def start(self) -> None:
        await self.consumer.start()
        await self.produser.start()

    async def stop(self) -> None:
        await self.consumer.stop()
        await self.produser.stop()

    async def start_consuming(self, topic: str):
        self.consumer.subscribe(topics=[topic])

        async for message in self.consumer:
            logging.warning(f'message.value: {message.value}')
            yield orjson.loads(message.value)

    async def stop_consuming(self) -> None:
        self.consumer.unsubscribe()

    async def send_message(self, topic: str, message: bytes, key:bytes):
        await self.produser.send(
            topic=topic,
            value=message,
            key=key
        )