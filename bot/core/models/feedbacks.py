from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixins import (
    AuthorTelegramIDMixin,
    IDMixin,
    CreatedAtMixin,
    UpdatedAtMixin,
)


class FeedbackModel(
    Base,
    IDMixin,
    AuthorTelegramIDMixin,
    CreatedAtMixin,
    UpdatedAtMixin,
):
    __tablename__ = "feedbacks"

    message: Mapped[str] = mapped_column(String(256))
    rate: Mapped[int]
    will_he_buy_more: Mapped[bool]


__all__ = [
    "FeedbackModel",
]
