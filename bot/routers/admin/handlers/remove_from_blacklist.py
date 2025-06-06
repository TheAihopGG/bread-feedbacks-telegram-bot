import re
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.methods import GetChat

from ....core.locales import get_locale_value
from ..forms import RemoveFromBlacklistForm
from ....services.admin.crud import remove_from_blacklist as remove_from_blacklist_crud
from ....core.database import sessionmaker
from ...global_keyboards import cancel_inline_keyboard


async def remove_from_blacklist_callback(
    call: CallbackQuery,
    state: FSMContext,
):
    if call.message:
        await state.clear()
        await state.set_state(RemoveFromBlacklistForm.user_id)

        await call.message.answer(
            get_locale_value("REMOVE_FROM_BLACKLIST_COMMAND_ANSWER_GET_USER_ID", "ru"),
            reply_markup=cancel_inline_keyboard,
        )


async def remove_from_blacklist_get_user_id(
    message: Message,
    state: FSMContext,
):
    if message.text:
        if re.search(r"^[0-9]+$", message.text):
            user_id = int(message.text)
            await state.update_data(user_id=user_id)
            data = await state.get_data()
            await state.clear()

            if GetChat(chat_id=user_id):
                async with sessionmaker() as session:
                    if await remove_from_blacklist_crud(session, data["user_id"]):
                        await message.answer(
                            get_locale_value(
                                "REMOVE_FROM_BLACKLIST_COMMAND_ANSWER_SUCCESS", "ru"
                            )
                        )
                    else:
                        await message.answer(
                            get_locale_value("SERVER_ERROR_ANSWER", "ru")
                        )
            else:
                await message.answer(
                    get_locale_value("USER_WAS_NOT_FOUND_ERROR_ANSWER", "ru"),
                    reply_markup=cancel_inline_keyboard,
                )
