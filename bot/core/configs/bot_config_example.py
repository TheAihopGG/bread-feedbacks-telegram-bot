from datetime import timezone
from dotenv import load_dotenv
from os import getenv

from . import BASE_DIR
from .env_config import ENV_FILENAME

assert load_dotenv(
    BASE_DIR / ENV_FILENAME
), f".env file was not found at {ENV_FILENAME}"

BOT_TZ = timezone.utc
BOT_API_TOKEN = getenv("BOT_API_TOKEN")
DATE_FORMATTER = "%Y/%m/%d, %H:%M:%S %Z"

ADMIN_ID = None
