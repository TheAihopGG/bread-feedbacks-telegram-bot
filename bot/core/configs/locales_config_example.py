from . import BASE_DIR

LOCALES_DIRNAME = BASE_DIR / "locales"
LOCALES = {
    "ru": LOCALES_DIRNAME / "ru.json",
    "en": LOCALES_DIRNAME / "en.json",
    "default": LOCALES_DIRNAME / "en.json",
}
