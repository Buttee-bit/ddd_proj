from dataclasses import dataclass
from backend.aplications.parser_tg.infra.brokers.base import BaseBroker
from faststream.kafka import KafkaBroker

@dataclass
class NewsKafkaBroker(BaseBroker):
    broker: KafkaBroker


    async def start(self) -> None:
        await self.broker.start()

    async def stop(self) -> None:
        await self.broker.close()

    async def start_consuming(self, topic: str): ...

    async def stop_consuming(self) -> None: ...

    async def send_message(self, topic: str, message):
        await self.broker.publish(
            message=message,
            topic=topic
        )
