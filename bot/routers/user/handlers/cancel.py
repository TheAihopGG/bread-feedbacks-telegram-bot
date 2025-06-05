from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from ....core.locales import get_locale_value


async def cancel_callback(
    call: CallbackQuery,
    state: FSMContext,
):
    if call.message:
        await state.clear()
        await state.set_state(None)
        await call.message.answer(get_locale_value("CANCEL_COMMAND_ANSWER", "ru"))
