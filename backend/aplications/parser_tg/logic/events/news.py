from dataclasses import dataclass
from typing import ClassVar

from backend.aplications.parser_tg.domain.events.news import NewMessageReceivedEvent
from backend.aplications.parser_tg.logic.events.base import EventHandler



@dataclass
class NewMessageReceivedEventHandler(EventHandler[NewMessageReceivedEvent, None]):
    async def handle(self, event: NewMessageReceivedEvent) -> None:
        ...
        # await self.message_broker.send_message(
        #     topic=self.broker_topic,
        #     value=convert_event_to_broker_message(event=event),
        #     key=event.chat_oid.encode(),
        # )
