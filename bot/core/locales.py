from orjson import loads
from .configs.locales_config import LOCALES, DEFAULT_LOCALE_NAME

locales_dict: dict[str, dict[str, str]] = {}
for locale_name, locale_filename in LOCALES.items():
    locales_dict[locale_name] = loads(open(locale_filename, "rb").read())


def get_locale_value(
    key: str,
    locale_name: str,
) -> str:
    if locale := locales_dict.get(key):
        if value := locale.get(locale_name):
            return value

    return get_default_locale_value(key)


def get_default_locale_value(
    key: str,
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
