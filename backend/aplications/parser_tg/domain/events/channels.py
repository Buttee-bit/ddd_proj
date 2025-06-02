from dataclasses import dataclass
from typing import ClassVar

from backend.aplications.parser_tg.domain.events.base import BaseEvent


@dataclass
class NewChannelReceivedEvent(BaseEvent):
    event_title: ClassVar[str] = 'New Message Received'

    link_channel: str
