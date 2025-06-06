from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    KeyboardButton,
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
