from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

cancel_inline_button = InlineKeyboardButton(
    text="Отмена",
    callback_data="cancel_callback",
)
