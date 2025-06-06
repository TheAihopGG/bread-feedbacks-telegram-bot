from aiogram.types import (
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    KeyboardButton,
)
from ..global_buttons import (
    cancel_inline_button,
    menu_inline_button,
)
from ...core.locales import get_locale_value

cancel_and_menu_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            cancel_inline_button,
            menu_inline_button,
        ]
    ]
)
menu_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            menu_inline_button,
        ]
    ]
)
yes_or_no_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=get_locale_value("YES", "ru")),
            KeyboardButton(text=get_locale_value("NO", "ru")),
        ]
    ],
    one_time_keyboard=True,
)

__all__ = [
    "menu_inline_keyboard",
    "yes_or_no_keyboard",
    "cancel_and_menu_inline_keyboard",
]
