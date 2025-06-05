from aiogram import Bot, Dispatcher
from .routers import (
    admin,
    user,
)

from .core.configs.bot_config import BOT_API_TOKEN

bot = Bot(token=BOT_API_TOKEN)
dp = Dispatcher()
dp.include_routers(
    admin.router,
    user.router,
)
__all__ = [
    "bot",
    "dp",
]
