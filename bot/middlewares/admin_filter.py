from typing import Awaitable, Callable, Any
from aiogram import BaseMiddleware
from aiogram.types import Message, TelegramObject

from ..services.admin.crud import is_admin
from ..core.locales import get_locale_value


class AdminFilterMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
        event: Message,  # type:ignore
        data: dict[str, Any],
    ) -> Any:
        if event.from_user:
            if is_admin(event.from_user.id):
                await event.answer(get_locale_value("ACCESS_DENIED", "ru"))
            else:
                return await handler(event, data)


__all__ = [
    "AdminFilterMiddleware",
]
