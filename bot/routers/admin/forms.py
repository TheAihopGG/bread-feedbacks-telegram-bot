from aiogram.fsm.state import State, StatesGroup


class AddToBlacklistForm(StatesGroup):
    user_id = State()


class RemoveFromBlacklistForm(StatesGroup):
    user_id = State()


class ShowBlacklistForm(StatesGroup):
    count = State()


__all__ = [
    "AddToBlacklistForm",
    "RemoveFromBlacklistForm",
]
