from . import BASE_DIR
from logging import INFO

SYSTEM_LOGS_FILENAME = BASE_DIR / "logs/system_logs.log"
SYSTEM_LOGS_LEVEL = INFO
SYSTEM_LOGS_ECHO = False
SYSTEM_LOGS_FORMATTER = "%(levelname)s: %(name)s: %(message)s - %(asctime)s"
