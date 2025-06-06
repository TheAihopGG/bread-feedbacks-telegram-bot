from aiogram.fsm.context import FSMContext
from aiogram.types import (
    CallbackQuery,
)
from ..keyboards import menu_inline_keyboard


from ....core.locales import get_locale_value


async def menu_callback(
    call: CallbackQuery,
    state: FSMContext,
):
    if call.message:
        await state.clear()
        await state.set_state(None)

        await call.message.answer(
            get_locale_value("MENU_COMMAND_ANSWER", "ru"),
            reply_markup=menu_inline_keyboard,
        )


__all__ = [
    "menu_callback",
]
