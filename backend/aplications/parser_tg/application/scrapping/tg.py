import logging
import pytz

from datetime import datetime
from telethon import TelegramClient, events
from faststream.kafka import KafkaBroker
from pydantic import BaseModel, Field

from backend.aplications.parser_tg.application.scrapping.dto import ListChannelDTO


class MessageDTO(BaseModel):
    message: str
    chat_oid: str
    time_publish: datetime
    time_recived: datetime = Field(default_factory=datetime.now)


class TgParsServices:
    def __init__(
        self,
        tg_client: TelegramClient,
        broker: KafkaBroker,
        topic: str,
    ):
        self.tg_client = tg_client
        self.broker = broker
        self.topic = topic

    async def start_listening(self, channels: ListChannelDTO):
        chats = [chat.url for chat in channels.channels]
        url_to_oid = {
            channel.url.split("/")[-1]: channel.oid for channel in channels.channels
        }
        await self.broker.start()
        await self.tg_client.start()

        @self.tg_client.on(events.NewMessage(chats=chats))
        async def handler(event: events.NewMessage.Event):
            logging.warning(f"event: {event}")
            chat = await event.get_chat()
            moscow_tz = pytz.timezone("Europe/Moscow")
            time_publish = event.date.astimezone(moscow_tz)
            oid = url_to_oid.get(chat.username, "unknown")
            logging.warning(f"event-publish")
            await self.broker.publish(
                topic=self.topic,
                message=MessageDTO(
                    message=event.text,
                    chat_oid=oid,
                    time_publish=time_publish,
                    time_recived=datetime.now(moscow_tz),
                ),
            )

        await self.tg_client.run_until_disconnected()
