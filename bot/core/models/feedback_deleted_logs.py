from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .mixins import IDMixin, CreatedAtMixin


class FeedbackDeletedLogModel(Base, IDMixin, CreatedAtMixin):
    __tablename__ = "feedback_deleted_logs"

    feedback_id: Mapped[int]


__all__ = [
    "FeedbackDeletedLogModel",
]
