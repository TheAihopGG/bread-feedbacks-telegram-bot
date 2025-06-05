from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.handlers import CallbackQueryHandler
from aiogram.types import CallbackQuery

from .handlers.start import start
from .handlers.cancel import cancel_callback
from .handlers.menu import menu
from .handlers.send_feedback import (
    send_feedback,
    send_feedback_step1,
    send_feedback_step2,
    send_feedback_step3,
)
from .forms import SendFeedbackForm
from ...middlewares import BlackListFilterMiddleware

router = Router(name="user")

router.message.middleware.register(BlackListFilterMiddleware())

router.message.register(start, CommandStart())
router.message.register(menu, Command("menu"))

router.message.register(send_feedback_step1, SendFeedbackForm.message)
router.message.register(send_feedback_step2, SendFeedbackForm.rate)
router.message.register(send_feedback_step3, SendFeedbackForm.will_he_by_more)

router.callback_query.register(
    send_feedback,
    F.data == "send_feedback_callback",
)

router.callback_query.register(
    cancel_callback,
    F.data == "cancel_callback",
)
