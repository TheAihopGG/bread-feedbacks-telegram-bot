from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixins import (
    TelegramIDMixin,
    IDMixin,
    CreatedAtMixin,
    UpdatedAtMixin,
)


class BlacklistUserModel(
    Base,
    IDMixin,
    TelegramIDMixin,
    CreatedAtMixin,
    UpdatedAtMixin,
):
    __tablename__ = "blacklist_users"

    reason: Mapped[str] = mapped_column(
        String(48),
        default="spam",
    )
