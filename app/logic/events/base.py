from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Generic, TypeVar

from app.domain.events import BaseEvent




ET = TypeVar("ET", bound=BaseEvent)
ER = TypeVar("ER", bound=Any)

@dataclass
class EventHandler(ABC, Generic[ET, ER]):
    # message_broker: BaseMessageBroker
    # connection_manager: BaseConnectionManager
    # broker_topic: str | None = None

    @abstractmethod
    def handle(self, event: ET) -> ER:
        ...
