from . import BASE_DIR

DEFAULT_LOCALE_NAME = "default"
LOCALES_DIRNAME = BASE_DIR / "bot/locales"
LOCALES = {
    "ru": LOCALES_DIRNAME / "ru.json",
    "en": LOCALES_DIRNAME / "en.json",
    DEFAULT_LOCALE_NAME: LOCALES_DIRNAME / "en.json",
}
