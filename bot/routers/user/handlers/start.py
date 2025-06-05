from aiogram.types import Message

from ....core.locales import get_locale_value


async def start(message: Message):
    await message.answer(get_locale_value("START_COMMAND_ANSWER", "ru"))
