from aiogram.types import (
    InlineKeyboardButton,
)


add_to_blacklist_inline_button = InlineKeyboardButton(
    text="Заблокировать пользователя",
    callback_data="add_to_blacklist_callback",
)
remove_from_blacklist_inline_button = InlineKeyboardButton(
    text="Разблокировать пользователя",
    callback_data="remove_from_blacklist_callback",
)
blacklist_inline_button = InlineKeyboardButton(
    text="Вывести чёрный список",
    callback_data="show_blacklist_callback",
)
