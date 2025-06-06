from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from ....core.locales import get_locale_value
from ..forms import ShowBlacklistForm
from ....services.admin.crud import get_blacklist
from ....core.database import sessionmaker
from ...global_keyboards import cancel_inline_keyboard


async def show_blacklist_callback(
    call: CallbackQuery,
    state: FSMContext,
):
    if call.message:
        await state.set_state(ShowBlacklistForm.count)

        await call.message.answer(
            get_locale_value("SHOW_BLACKLIST_COMMAND_ANSWER_GET_COUNT", "ru"),
            reply_markup=cancel_inline_keyboard,
        )


async def show_blacklist_get_count(
    message: Message,
    state: FSMContext,
):
    if message.text:
        if message.text.isdigit():
            await state.update_data(count=int(message.text))
            data = await state.get_data()
            await state.clear()
            async with sessionmaker() as session:
                await message.answer(
                    get_locale_value(
                        "SHOW_BLACKLIST_COMMAND_ANSWER_SUCCESS", "ru"
                    ).format(
                        "\n- ".join(
                            [
                                str(value)
                                for value in [
                                    model.user_telegram_id
                                    for model in await get_blacklist(
                                        session, data["count"]
                                    )
                                ]
                            ]
                        )
                        or get_locale_value("EMPTY_BLACKLIST_COMMAND_ANSWER", "ru")
                    ),
                )
        else:
            await message.answer(
                get_locale_value("INVALID_VALUE_ERROR_ANSWER", "ru"),
                reply_markup=cancel_inline_keyboard,
            )
