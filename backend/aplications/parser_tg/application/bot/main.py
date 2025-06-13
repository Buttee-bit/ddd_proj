import asyncio
import logging
from punq import Container
from aiogram import Bot, Dispatcher, html
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from backend.aplications.parser_tg.logic.init import init_conatainer
from backend.aplications.parser_tg.setings.setting import Setings



async def start() -> None:
    container: Container = init_conatainer()
    Settings: Setings = container.resolve(Setings)
    bot: Bot = Bot(
        token=Settings.BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp: Dispatcher = Dispatcher()
    logging.warning(f'bot: {bot}')
    @dp.message(CommandStart())
    async def command_start_handler(message: Message) -> None:
        logging.warning(f': {message.from_user.id}')
        await message.answer(f"Hello, {html.bold(message.from_user.full_name)}! {message.from_user.id}")

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(start())