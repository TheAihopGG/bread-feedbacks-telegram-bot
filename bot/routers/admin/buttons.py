from aiogram.types import (
    InlineKeyboardButton,
)
from ...core.locales import get_locale_value


add_to_blacklist_inline_button = InlineKeyboardButton(
    text=get_locale_value("ADD_TO_BLACKLIST_MENU_OPTION_NAME", "ru"),
    callback_data="add_to_blacklist_callback",
)
remove_from_blacklist_inline_button = InlineKeyboardButton(
    text=get_locale_value("REMOVE_FROM_BLACKLIST_MENU_OPTION_NAME", "ru"),
    callback_data="remove_from_blacklist_callback",
)
blacklist_inline_button = InlineKeyboardButton(
    text=get_locale_value("SHOW_BLACKLIST_MENU_OPTION_NAME", "ru"),
    callback_data="show_blacklist_callback",
)
