from aiogram.types import Message
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
)

from ..buttons import send_feedback_inline_button
from ...global_buttons import menu_inline_button
from ....core.locales import get_locale_value


async def start(message: Message):
    await message.answer(
        get_locale_value("START_COMMAND_ANSWER", "ru"),
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    send_feedback_inline_button,
                    menu_inline_button,
                ]
            ]
        ),
    )


__all__ = [
    "start",
]
