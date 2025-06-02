from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import AsyncIterable


@dataclass
class BaseBroker(ABC):

    @abstractmethod
    async def start(self): ...

    @abstractmethod
    async def stop(self): ...

    @abstractmethod
    async def start_consuming(self, topic: str): ...

    @abstractmethod
    async def stop_consuming(self): ...

    @abstractmethod
    async def send_message(self, topic: str, message): ...
