from datetime import datetime
from sqlalchemy import func
from sqlalchemy.orm import declared_attr, Mapped, mapped_column

from ...core.configs.bot_config import BOT_TZ


class IDMixin:
    @declared_attr
    def id(cls) -> Mapped[int]:
        return mapped_column(primary_key=True, index=True)


class AuthorTelegramIDMixin:
    _telegram_id_unique: bool = True

    @declared_attr
    def author_telegram_id(cls) -> Mapped[int]:
        return mapped_column(unique=cls._telegram_id_unique)


class UserTelegramIDMixin:
    _telegram_id_unique: bool = True

    @declared_attr
    def user_telegram_id(cls) -> Mapped[int]:
        return mapped_column(unique=cls._telegram_id_unique)


class CreatedAtMixin:
    @declared_attr
    def created_at(cls) -> Mapped[datetime]:
        return mapped_column(
            default=lambda: datetime.now(BOT_TZ),
            server_default=func.now(),
        )


class UpdatedAtMixin:
    @declared_attr
    def updated_at(cls) -> Mapped[datetime]:
        return mapped_column(
            default=lambda: datetime.now(BOT_TZ),
            onupdate=lambda: datetime.now(BOT_TZ),
        )


__all__ = [
    "IDMixin",
    "AuthorTelegramIDMixin",
    "CreatedAtMixin",
    "UpdatedAtMixin",
]
