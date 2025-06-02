import logging
import pytz

from datetime import datetime
from telethon import TelegramClient, events
from faststream.kafka import KafkaBroker
from pydantic import BaseModel, Field

from backend.aplications.parser_tg.application.scrapping.dto import ListChannelDTO
from backend.aplications.parser_tg.domain.entity.news.news import News
from dataclasses import dataclass

from backend.aplications.parser_tg.infra.brokers.base import BaseBroker


class MessageDTO(BaseModel):
    message: str
    chat_oid: str
    time_publish: datetime
    time_recived: datetime = Field(default_factory=datetime.now)


@dataclass
class TgParsServices:
    tg_client: TelegramClient
    broker: BaseBroker

    async def start_listening(self, channels: ListChannelDTO):
        chats = [chat.url for chat in channels.channels]
        url_to_oid = {
            channel.url.split("/")[-1]: channel.oid for channel in channels.channels
        }

        @self.tg_client.on(events.NewMessage(chats=chats))
        async def handler(event: events.NewMessage.Event):
            logging.warning(f'event: {event}')
            chat = await event.get_chat()
            moscow_tz = pytz.timezone("Europe/Moscow")
            time_publish = event.date.astimezone(moscow_tz)
            oid = url_to_oid.get(chat.username, "unknown")
            news = News(
                title=event.text[:50],
                text=event.text,
                published_at=time_publish,
                oid_channel=oid,
            )
            await self.broker.send_message(
                topic='telegram_messages',
                message=news,
            )

        await self.tg_client.run_until_disconnected()

    async def subscribe_to_channel(self): ...