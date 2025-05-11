import logging
import orjson

from dataclasses import dataclass
from typing import AsyncIterable



from backend.aplications.parser_tg.infra.brokers.base import BaseBroker
from faststream.kafka import KafkaBroker


@dataclass
class NewsKafkaBroker(BaseBroker):
    broker: KafkaBroker

    async def start(self) -> None:
        logging.warning(f'await self.broker.start()')
        await self.broker.start()

    async def stop(self) -> None:
        await self.broker.close()

    async def start_consuming(self, topic:str) -> AsyncIterable[dict]:
        await self.broker.subscriber(topic=topic)
        async for message in self.broker:
            yield orjson.loads(message)

    async def stop_consuming(self) -> None:
        ...

    async def send_message(self):
        ...
