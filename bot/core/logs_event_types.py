from enum import auto, StrEnum


class LogEventType(StrEnum):
    FEEDBACK_WAS_SENDED = auto()
    USER_WAS_ADDED_TO_BLACKLIST = auto()
    USER_WAS_REMOVED_FROM_BLACKLIST = auto()


__all__ = [
    "LogEventType",
]
