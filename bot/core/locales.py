from orjson import loads
from typing import Literal

from ..core.system_logger import system_logger_decorator
from .configs.locales_config import LOCALES, DEFAULT_LOCALE_NAME


type LocaleKeys = Literal[
    "START_COMMAND_ANSWER",
    "MENU_COMMAND_ANSWER",
    "SEND_FEEDBACK_COMMAND_ANSWER_GET_MESSAGE",
    "SEND_FEEDBACK_COMMAND_ANSWER_GET_RATE",
    "SEND_FEEDBACK_COMMAND_ANSWER_GET_WILL_HE_BY_MORE",
    "SEND_FEEDBACK_COMMAND_ANSWER_SUCCESS",
    "CANCEL_COMMAND_ANSWER",
    "ADMIN_PANEL_COMMAND_ANSWER",
    "ADD_TO_BLACKLIST_COMMAND_ANSWER_GET_USER_ID",
    "ADD_TO_BLACKLIST_COMMAND_ANSWER_SUCCESS",
    "REMOVE_FROM_BLACKLIST_COMMAND_ANSWER_GET_USER_ID",
    "REMOVE_FROM_BLACKLIST_COMMAND_ANSWER_SUCCESS",
    "SHOW_BLACKLIST_COMMAND_ANSWER_GET_COUNT",
    "SHOW_BLACKLIST_COMMAND_ANSWER_SUCCESS",
    "TEXT_IS_TOO_LONG_ERROR_ANSWER",
    "INVALID_VALUE_ERROR_ANSWER",
    "USER_WAS_NOT_FOUND_ERROR_ANSWER",
    "USER_IN_BLACKLIST",
    "ACCESS_DENIED",
    "ENTER_TEXT_FROM_KEYBOARD",
    "SERVER_ERROR_ANSWER",
    "YES",
    "NO",
    "ADD_TO_BLACKLIST_MENU_OPTION_NAME",
    "REMOVE_FROM_BLACKLIST_MENU_OPTION_NAME",
    "SHOW_BLACKLIST_MENU_OPTION_NAME",
]


locales_dict: dict[str, dict[str, str]] = {}
for locale_name, locale_filename in LOCALES.items():
    locales_dict[locale_name] = loads(open(locale_filename, "rb").read())


def get_locale_value(
    key: LocaleKeys,
    locale_name: str,
) -> str:
    if locale := locales_dict.get(locale_name):
        if value := locale.get(key):
            return value

    return get_default_locale_value(key)


def get_default_locale_value(
    key: LocaleKeys,
    default_locale_name: str = DEFAULT_LOCALE_NAME,
) -> str:
    if default_locale := locales_dict.get(default_locale_name):
        if default_value := default_locale.get(key):
            return default_value
        else:
            raise KeyError(
                f"Key '{key}'was not found in locale '{default_locale_name}'"
            )
    else:
        raise KeyError(f"Locale '{default_locale_name}' was not found")


__all__ = [
    "get_locale_value",
    "get_default_locale_value",
]
