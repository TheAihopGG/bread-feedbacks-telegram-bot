import re
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    Message,
    CallbackQuery,
    ReplyKeyboardMarkup,
    KeyboardButton,
)
from ..keyboards import cancel_and_menu_inline_keyboard, yes_or_no_keyboard

from ....core.locales import get_locale_value
from ....core.database import sessionmaker
from ....services.feedback.crud import send_feedback as send_feedback_crud
from ....core.configs.bot_config import FEEDBACK_MAX_LEN
from ..forms import SendFeedbackForm


async def send_feedback(
    call: CallbackQuery,
    state: FSMContext,
):
    if call.message:
        await state.clear()
        await state.set_state(SendFeedbackForm.message)

        await call.message.answer(
            get_locale_value("SEND_FEEDBACK_COMMAND_ANSWER_GET_MESSAGE", "ru"),
            reply_markup=cancel_and_menu_inline_keyboard,
        )


async def send_feedback_get_message(
    message: Message,
    state: FSMContext,
):
    if message.text:
        if len(message.text) < FEEDBACK_MAX_LEN:
            await state.update_data(message=message.text)
            await state.set_state(SendFeedbackForm.rate)

            await message.answer(
                get_locale_value("SEND_FEEDBACK_COMMAND_ANSWER_GET_RATE", "ru"),
                reply_markup=cancel_and_menu_inline_keyboard,
            )
            await message.answer(
                get_locale_value("ENTER_TEXT_FROM_KEYBOARD", "ru"),
                reply_markup=ReplyKeyboardMarkup(
                    keyboard=[
                        [
                            KeyboardButton(text="1"),
                            KeyboardButton(text="2"),
                            KeyboardButton(text="3"),
                            KeyboardButton(text="4"),
                            KeyboardButton(text="5"),
                        ]
                    ],
                    one_time_keyboard=True,
                ),
            )
        else:
            await message.answer(
                get_locale_value(
                    "TEXT_IS_TOO_LONG_ERROR_ANSWER",
                    "ru",
                ),
                reply_markup=cancel_and_menu_inline_keyboard,
            )


async def send_feedback_get_rate(
    message: Message,
    state: FSMContext,
):
    if message.text:
        if re.search(r"^[12345]{1}$", message.text):
            rate = int(message.text)
            await state.update_data(rate=rate)
            await state.set_state(SendFeedbackForm.will_he_by_more)

            await message.answer(
                get_locale_value(
                    "SEND_FEEDBACK_COMMAND_ANSWER_GET_WILL_HE_BY_MORE", "ru"
                ),
                reply_markup=cancel_and_menu_inline_keyboard,
            )
            await message.answer(
                get_locale_value("ENTER_TEXT_FROM_KEYBOARD", "ru"),
                reply_markup=yes_or_no_keyboard,
            )
        else:
            await message.answer(
                get_locale_value("INVALID_VALUE_ERROR_ANSWER", "ru"),
                reply_markup=cancel_and_menu_inline_keyboard,
            )


async def send_feedback_get_will_he_by_more(
    message: Message,
    state: FSMContext,
):
    if message.text and message.from_user:
        if message.text == get_locale_value(
            "YES",
            "ru",
        ) or message.text == get_locale_value(
            "NO",
            "ru",
        ):
            await state.update_data(
                will_he_by_more=message.text
                == get_locale_value(
                    "YES",
                    "ru",
                )
            )
            data = await state.get_data()
            await state.clear()

            async with sessionmaker() as session:
                await send_feedback_crud(
                    session,
                    message=data["message"],
                    rate=data["rate"],
                    will_he_buy_more=data["will_he_by_more"],
                    author_telegram_id=message.from_user.id,
                    bot=message.bot,  # type: ignore
                )
                await message.answer(
                    get_locale_value("SEND_FEEDBACK_COMMAND_ANSWER_SUCCESS", "ru")
                )
        else:
            await message.answer(
                get_locale_value("INVALID_VALUE_ERROR_ANSWER", "ru"),
                reply_markup=cancel_and_menu_inline_keyboard,
            )


__all__ = [
    "send_feedback",
    "send_feedback_get_message",
    "send_feedback_get_rate",
    "send_feedback_get_will_he_by_more",
]
