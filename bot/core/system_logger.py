from logging import (
    basicConfig,
    getLogger,
    StreamHandler,
    FileHandler,
)

from .configs.system_logger_config import (
    SYSTEM_LOGS_FORMATTER,
    SYSTEM_LOGS_LEVEL,
    SYSTEM_LOGS_FILENAME,
)

system_logger = getLogger(__name__)
basicConfig(
    format=SYSTEM_LOGS_FORMATTER,
    level=SYSTEM_LOGS_LEVEL,
    handlers=[
        FileHandler(SYSTEM_LOGS_FILENAME, mode="w"),
        StreamHandler(),
    ],
)

__all__ = [
    "system_logger_decorator",
    "async_system_logger_decorator",
    "system_logger",
]
