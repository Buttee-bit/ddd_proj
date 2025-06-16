import logging
import pytz

from datetime import datetime
from telethon import TelegramClient, events
from faststream.kafka import KafkaBroker
from pydantic import BaseModel, Field

from backend.aplications.parser_tg.application.scrapping.dto import ListChannelDTO
from backend.aplications.parser_tg.domain.entity.news.news import News
from dataclasses import dataclass, field

from backend.aplications.parser_tg.infra.brokers.base import BaseBroker
from telethon.tl.functions.channels import JoinChannelRequest, GetFullChannelRequest
from telethon.tl.types.messages import ChatFull

from backend.aplications.parser_tg.infra.repositoryes.channels.base import BaseChannelRepository

class MessageDTO(BaseModel):
    message: str
    chat_oid: str
    time_publish: datetime
    time_recived: datetime = Field(default_factory=datetime.now)


@dataclass
class TgParsServices:
    tg_client: TelegramClient
    broker: BaseBroker
    channels_repo: BaseChannelRepository
    _list_channels: list = field(default_factory=list, kw_only=True)
    _handler: events.NewMessage.Event | None = field(default=None, kw_only=True)  # Track the current handler

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
            news = News(
                title=event.text[:50],
                text=event.text,
                published_at=time_publish,
                id_channel=event._chat_peer.channel_id,
            )
            await self.broker.send_message(
                message=news,
                topic='telegram_messages',
            )

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
        self._list_channels = [await self.tg_client.get_entity(channel.url) for channel in list_channels]
        logging.warning(f'Updated channels: {len(self._list_channels)}')