from dataclasses import dataclass
from typing import ClassVar

from app.domain.events.base import BaseEvent


@dataclass
class NewChannelReceivedEvent(BaseEvent):
    event_title: ClassVar[str] = 'New Message Received'

    link_channel: str
