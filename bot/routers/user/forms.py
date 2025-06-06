from aiogram.fsm.state import State, StatesGroup


class SendFeedbackForm(StatesGroup):
    message = State()
    rate = State()
    will_he_by_more = State()


__all__ = [
    "SendFeedbackForm",
]
