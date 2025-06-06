import re
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, Message
from aiogram.methods import GetChat

from ....core.locales import get_locale_value
from ....core.database import sessionmaker
from ..forms import AddToBlacklistForm
from ....services.admin.crud import add_to_blacklist as add_to_blacklist_crud
from ...global_buttons import cancel_inline_button


async def add_to_blacklist_callback(
    call: CallbackQuery,
    state: FSMContext,
):
    if call.message:
        await state.clear()
        await state.set_state(AddToBlacklistForm.user_id)

        await call.message.answer(
            get_locale_value("ADD_TO_BLACKLIST_COMMAND_ANSWER_GET_USER_ID", "ru"),
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        cancel_inline_button,
                    ]
                ]
            ),
        )


async def add_to_blacklist_get_user_id(
    message: Message,
    state: FSMContext,
):
    if message.text:
        if message.text.isdigit():
            user_id = int(message.text)
            if GetChat(chat_id=user_id):
                await state.update_data(user_id=user_id)
                data = await state.get_data()
                await state.clear()

                async with sessionmaker() as session:
                    if await add_to_blacklist_crud(session, data["user_id"]):
                        await message.answer(
                            get_locale_value(
                                "ADD_TO_BLACKLIST_COMMAND_ANSWER_SUCCESS", "ru"
                            )
                        )
                    else:
                        await message.answer(
                            get_locale_value("SERVER_ERROR_ANSWER", "ru")
                        )
            else:
                await message.answer(
                    get_locale_value("USER_WAS_NOT_FOUND_ERROR_ANSWER", "ru")
                )
