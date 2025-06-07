from datetime import timezone
from dotenv import load_dotenv
from os import getenv

from . import BASE_DIR
from .env_config import ENV_FILENAME

assert load_dotenv(
    BASE_DIR / ENV_FILENAME
), f".env file was not found at {ENV_FILENAME}"

BOT_TZ = timezone.utc
BOT_API_TOKEN = str(getenv("BOT_API_TOKEN", ""))
DATE_FORMATTER = "%Y/%m/%d, %H:%M:%S %Z"

FEEDBACK_MAX_LEN = 256

ADMIN_ID = 6798100760

assert BOT_API_TOKEN, "You need to add your BOT_API_TOKEN into .env file"
assert ADMIN_ID, "You need to specify your ADMIN_ID in bot_config.py"
