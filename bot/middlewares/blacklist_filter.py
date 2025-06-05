from typing import Awaitable, Callable, Any
from aiogram import BaseMiddleware
from aiogram.types import Message, TelegramObject

from ..services.admin.crud import is_in_blacklist
from ..core.locales import get_locale_value
from ..core.database import sessionmaker


class BlackListFilterMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
        event: Message,  # type:ignore
        data: dict[str, Any],
    ) -> Any:
        if event.from_user:
            async with sessionmaker() as session:
                if blacklist_user_object := await is_in_blacklist(
                    session, event.from_user.id
                ):
                    await event.answer(
                        get_locale_value("USER_IN_BLACKLIST", "ru").format(
                            blacklist_user_object.reason
                        )
                    )
                else:
                    return await handler(event, data)


__all__ = [
    "BlackListFilterMiddleware",
]
