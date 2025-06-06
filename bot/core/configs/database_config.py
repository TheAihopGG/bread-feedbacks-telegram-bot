from . import BASE_DIR

SQLALCHEMY_DRIVER = "sqlite+aiosqlite"

DATABASES_DIRNAME = BASE_DIR / "data"
PROD_DATABASE_URL = f"{SQLALCHEMY_DRIVER}:///data/prod.db"
DEV_DATABASE_URL = f"{SQLALCHEMY_DRIVER}:///data/dev.db"
DATABASE_DEV_MODE = True

PROD_DATABASE_ECHO = True
DEV_DATABASE_ECHO = True
