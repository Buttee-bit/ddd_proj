import logging
import pytz

from dataclasses import dataclass, field
from datetime import datetime
from telethon import TelegramClient, events
from pydantic import BaseModel, Field


from app.domain.entity.news.news import News
from app.domain.values.news.title import Title
from app.domain.values.news.text import Text

from app.infra.brokers.base import BaseBroker
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.types.messages import ChatFull

from app.infra.repositoryes.channels.base import (
    BaseChannelRepository,
)


@dataclass
class TgParsServices:
    tg_client: TelegramClient
    broker: BaseBroker
    channels_repo: BaseChannelRepository
    _list_channels: list = field(default_factory=list, kw_only=True)
    _handler: events.NewMessage.Event | None = field(default=None, kw_only=True)

    async def start_listening(self):
        await self._update_list_channels()
        await self._register_handler()
        await self.tg_client.run_until_disconnected()

    async def _register_handler(self):
        if self._handler:
            self.tg_client.remove_event_handler(self._handler)

        @self.tg_client.on(events.NewMessage(chats=self._list_channels))
        async def handler(event: events.NewMessage.Event):
            moscow_tz = pytz.timezone("Europe/Moscow")
            time_publish = event.date.astimezone(moscow_tz)

            try:
                title = Title(event.text[:50]).as_generic_type()
                text = Text(event.text).as_generic_type()
                news = News(
                    title=title,
                    text=text,
                    published_at=time_publish,
                    id_channel=event._chat_peer.channel_id,
                )
                await self.broker.send_message(
                    message=news,
                    topic="telegram_messages",
                )
            except Exception as e:
                # TODO Херня какая-то
                logging.error(f"event: {event}\nОшибка: {e.message}")

        self._handler = handler

    async def subscribe_to_channel(self, channel_url) -> ChatFull:
        entity = await self.tg_client.get_entity(channel_url)
        try:
            await self.tg_client(JoinChannelRequest(channel=entity))
            await self._update_list_channels()
            await self._register_handler()
        except Exception as e:
            logging.error(e)

    async def _update_list_channels(self) -> None:
        list_channels = await self.channels_repo.get_all_channels()
        self._list_channels = [
            await self.tg_client.get_entity(channel.url) for channel in list_channels
        ]
        logging.warning(f"Updated channels: {len(self._list_channels)}")
