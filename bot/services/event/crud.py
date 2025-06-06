from sqlalchemy.ext.asyncio import AsyncSession

from ...core.models import EventModel
from ...core.logs_event_types import LogEventType


async def log_add_event(
    session: AsyncSession,
    *,
    event_type: LogEventType,
    metadata: dict,
) -> EventModel:
    event = EventModel(
        type=event_type,
        metadata_=metadata,
    )
    session.add(event)
    await session.commit()

    return event


__all__ = [
    "log_add_event",
]
