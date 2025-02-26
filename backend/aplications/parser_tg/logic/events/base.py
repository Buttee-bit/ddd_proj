from abc import ABC
from dataclasses import dataclass
from typing import Any, TypeVar


@dataclass(frozen=True)
class BaseEvent(ABC):
    ...

ET = TypeVar("ET", bound=BaseEvent)
ER = TypeVar("ER", bound=Any)

@dataclass
class BaseEventHandler(ABC):
    def handle(self, event: ET) -> ER:
        ...