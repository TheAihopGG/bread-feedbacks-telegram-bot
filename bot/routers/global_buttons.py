from aiogram.types import InlineKeyboardButton

cancel_inline_button = InlineKeyboardButton(
    text="Отмена",
    callback_data="cancel_callback",
)
menu_inline_button = InlineKeyboardButton(
    text="Меню",
    callback_data="menu_callback",
)

__all__ = [
    "cancel_inline_button",
    "menu_inline_button",
]
