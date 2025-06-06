from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import JSON

from .base import Base
from .mixins import CreatedAtMixin, IDMixin
from ..logs_event_types import LogEventType


class EventModel(Base, CreatedAtMixin, IDMixin):
    __tablename__ = "events"

    type: Mapped[LogEventType]
    metadata_: Mapped[dict] = mapped_column(JSON())


__all__ = [
    "EventModel",
]
