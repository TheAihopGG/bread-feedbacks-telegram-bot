from aiogram import Router, F
from aiogram.filters import CommandStart

from .handlers.start import start
from .handlers.cancel import cancel_callback
from .handlers.menu import menu_callback
from .handlers.send_feedback import (
    send_feedback,
    send_feedback_get_message,
    send_feedback_get_rate,
    send_feedback_get_will_he_by_more,
)
from .forms import SendFeedbackForm
from ...middlewares import BlackListFilterMiddleware

router = Router(name="user")

router.message.middleware.register(BlackListFilterMiddleware())

router.message.register(
    start,
    CommandStart(),
)

router.message.register(
    send_feedback_get_message,
    SendFeedbackForm.message,
)
router.message.register(
    send_feedback_get_rate,
    SendFeedbackForm.rate,
)
router.message.register(
    send_feedback_get_will_he_by_more,
    SendFeedbackForm.will_he_by_more,
)

router.callback_query.register(
    send_feedback,
    F.data == "send_feedback_callback",
)

router.callback_query.register(
    cancel_callback,
    F.data == "cancel_callback",
)

router.callback_query.register(
    menu_callback,
    F.data == "menu_callback",
)

__all__ = [
    "router",
]
