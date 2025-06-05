import re
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    KeyboardButton,
)
from ..keyboards import cancel_inline_button

from ....core.locales import get_locale_value
from ....core.database import sessionmaker
from ....services.feedback.crud import send_feedback as send_feedback_crud
from ..forms import SendFeedbackForm


async def send_feedback(call: CallbackQuery, state: FSMContext):
    if call.message:
        await state.clear()
        await state.set_state(SendFeedbackForm.message)
        await call.message.answer(
            get_locale_value("SEND_FEEDBACK_ANSWER", "ru"),
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        cancel_inline_button,
                    ]
                ],
            ),
        )


async def send_feedback_step1(message: Message, state: FSMContext):
    if message.text:
        if len(message.text) < 256:
            await state.update_data(message=message.text)
            await state.set_state(SendFeedbackForm.rate)
            await message.answer(
                get_locale_value("SEND_FEEDBACK_ANSWER_STEP_1", "ru"),
                reply_markup=InlineKeyboardMarkup(
                    inline_keyboard=[
                        [
                            cancel_inline_button,
                        ]
                    ]
                ),
            )
            await message.answer(
                "Введите значение на клавиатуре",
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
                reply_markup=InlineKeyboardMarkup(
                    inline_keyboard=[
                        [
                            cancel_inline_button,
                        ]
                    ]
                ),
            )


async def send_feedback_step2(message: Message, state: FSMContext):
    if message.text:
        if re.search(r"^[12345]{1}$", message.text):
            rate = int(message.text)
            await state.update_data(rate=rate)
            await state.set_state(SendFeedbackForm.will_he_by_more)
            await message.answer(
                get_locale_value("SEND_FEEDBACK_ANSWER_STEP_2", "ru"),
                reply_markup=InlineKeyboardMarkup(
                    inline_keyboard=[
                        [
                            cancel_inline_button,
                        ]
                    ]
                ),
            )
            await message.answer(
                "Введите значение на клавиатуре",
                reply_markup=ReplyKeyboardMarkup(
                    keyboard=[
                        [
                            KeyboardButton(text="Да"),
                            KeyboardButton(text="Нет"),
                        ]
                    ],
                    one_time_keyboard=True,
                ),
            )
        else:
            await message.answer(
                get_locale_value("INVALID_VALUE_ERROR_ANSWER", "ru"),
                reply_markup=InlineKeyboardMarkup(
                    inline_keyboard=[
                        [
                            cancel_inline_button,
                        ]
                    ]
                ),
            )


async def send_feedback_step3(message: Message, state: FSMContext):
    if message.text and message.from_user:
        if re.search(r"^Да|Нет$", message.text):
            will_he_by_more = message.text == "y"
            await state.update_data(will_he_by_more=will_he_by_more)
            data = await state.get_data()
            await state.clear()
            async with sessionmaker() as session:
                if await send_feedback_crud(
                    session,
                    message=data["message"],
                    rate=data["rate"],
                    will_he_buy_more=data["will_he_by_more"],
                    author_telegram_id=message.from_user.id,
                ):
                    await message.answer(
                        get_locale_value("SEND_FEEDBACK_ANSWER_STEP_3", "ru")
                    )

        else:
            await message.answer(
                get_locale_value("INVALID_VALUE_ERROR_ANSWER", "ru"),
                reply_markup=InlineKeyboardMarkup(
                    inline_keyboard=[
                        [
                            cancel_inline_button,
                        ]
                    ]
                ),
            )
