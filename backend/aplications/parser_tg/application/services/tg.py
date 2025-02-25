import logging
from datetime import datetime
import pytz  # Используем pytz вместо zoneinfo
from telethon import TelegramClient, events
from typing import Callable, Awaitable

class TgParsServices:
    def __init__(
        self,
        tg_client: TelegramClient,
        watcher_groups: list[str],
        message_handler: Callable[[str], Awaitable[None]]
    ):
        self.tg_client = tg_client
        self.watcher_groups = watcher_groups
        self.message_handler = message_handler

    async def start_listening(self):
        @self.tg_client.on(events.NewMessage(chats=self.watcher_groups))
        async def handler(event: events.NewMessage.Event):
            logging.warning(f"Получено сообщение: {event}")
            timezone = pytz.timezone("Europe/Moscow")
            local_time = event.date.replace(tzinfo=pytz.utc).astimezone(timezone)

            logging.warning(f"Локальное время сообщения: {local_time}")

            chat = await event.get_chat()
            logging.warning(f"Чат: {chat.title if hasattr(chat, 'title') else 'Private Chat'}")
            await self.message_handler(event.text)

        # Запуск клиента Telegram
        await self.tg_client.start()
        await self.tg_client.run_until_disconnected()