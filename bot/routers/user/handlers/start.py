from aiogram.types import Message
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
)

from ..keyboards import menu_inline_button
from ....core.locales import get_locale_value


async def start(message: Message):
    await message.answer(
        get_locale_value("START_COMMAND_ANSWER", "ru"),
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    menu_inline_button,
                ]
            ]
        ),
    )


__all__ = [
    "start",
]
