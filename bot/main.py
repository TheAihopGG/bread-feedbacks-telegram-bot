from aiogram import Bot, Dispatcher
from .core.system_logger import system_logger
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
system_logger.info("Bot initialized")
__all__ = [
    "bot",
    "dp",
]
