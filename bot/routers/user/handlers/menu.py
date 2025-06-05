from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import (
    ReplyKeyboardRemove,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)


from ....core.locales import get_locale_value


async def menu(message: Message):
    await message.answer(
        get_locale_value("MENU_COMMAND_ANSWER", "ru"),
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="Оставить отзыв",
                        callback_data="send_feedback_callback",
                    ),
                ]
            ]
        ),
    )
