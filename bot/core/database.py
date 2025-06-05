from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
)

from .configs.database_config import (
    PROD_DATABASE_URL,
    PROD_DATABASE_ECHO,
    DEV_DATABASE_ECHO,
    DEV_DATABASE_URL,
    DATABASE_DEV_MODE,
)

engine = create_async_engine(
    url=DEV_DATABASE_URL if DATABASE_DEV_MODE else PROD_DATABASE_URL,
    echo=DEV_DATABASE_ECHO if DATABASE_DEV_MODE else PROD_DATABASE_ECHO,
)
sessionmaker = async_sessionmaker(
    engine,
    expire_on_commit=False,
    autoflush=True,
)
__all__ = [
    "engine",
    "sessionmaker",
]
