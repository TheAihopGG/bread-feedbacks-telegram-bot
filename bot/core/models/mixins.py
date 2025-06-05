from datetime import datetime
from sqlalchemy import func
from sqlalchemy.orm import declared_attr, Mapped, mapped_column

from ..configs.bot_config import DATE_FORMATTER


class IDMixin:
    @declared_attr
    def id(cls) -> Mapped[int]:
        return mapped_column(primary_key=True, index=True)


class TelegramIDMixin:
    _telegram_id_unique: bool = True

    @declared_attr
    def telegram_id(cls) -> Mapped[int]:
        return mapped_column(unique=cls._telegram_id_unique)


class CreatedAtMixin:
    @declared_attr
    def created_at(cls) -> Mapped[datetime]:
        return mapped_column(default=datetime.now, server_default=func.now())


class UpdatedAtMixin:
    @declared_attr
    def updated_at(cls) -> Mapped[datetime]:
        return mapped_column(default=datetime.now, onupdate=datetime.now)


__all__ = [
    "IDMixin",
    "TelegramIDMixin",
    "CreatedAtMixin",
    "UpdatedAtMixin",
]
