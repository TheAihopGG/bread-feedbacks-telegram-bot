from aiogram.types import Message, InlineKeyboardMarkup

from ....core.locales import get_locale_value
from ..buttons import (
    add_to_blacklist_inline_button,
    blacklist_inline_button,
    remove_from_blacklist_inline_button,
)


async def admin_panel(message: Message):
    await message.answer(
        get_locale_value("ADMIN_PANEL_COMMAND_ANSWER", "ru"),
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    add_to_blacklist_inline_button,
                    blacklist_inline_button,
                    remove_from_blacklist_inline_button,
                ],
            ],
        ),
    )


__all__ = [
    "admin_panel",
]
