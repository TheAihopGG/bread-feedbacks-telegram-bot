from aiogram.types import InlineKeyboardMarkup

from .global_buttons import cancel_inline_button

cancel_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            cancel_inline_button,
        ]
    ]
)
