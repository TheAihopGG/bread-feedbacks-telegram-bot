from aiogram.types import InlineKeyboardButton

send_feedback_inline_button = InlineKeyboardButton(
    text="Отправить отзыв",
    callback_data="send_feedback_callback",
)
__all__ = [
    "send_feedback_inline_button",
]
