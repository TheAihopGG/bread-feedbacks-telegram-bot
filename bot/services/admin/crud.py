from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from ...core.database import sessionmaker
from ...core.models import BlacklistUserModel
from ...core.configs.bot_config import ADMIN_ID
from ...core.logs_event_types import LogEventType
from ...services.event.crud import log_add_event


async def is_in_blacklist(
    session: AsyncSession,
    telegram_id: int,
) -> BlacklistUserModel | None:
    return (
        await session.execute(
            select(
                BlacklistUserModel,
            ).where(
                BlacklistUserModel.user_telegram_id == telegram_id,
            )
        )
    ).scalar_one_or_none()


async def add_to_blacklist(
    session: AsyncSession,
    telegram_id: int,
) -> bool:
    if blacklist_user_object := await is_in_blacklist(session, telegram_id):
        return False
    blacklist_user_object = BlacklistUserModel(
        user_telegram_id=telegram_id,
    )

    session.add(blacklist_user_object)
    await session.commit()

    await log_add_event(
        session,
        event_type=LogEventType.USER_WAS_ADDED_TO_BLACKLIST,
        metadata={"user_telegram_id": telegram_id},
    )

    return True


async def remove_from_blacklist(
    session: AsyncSession,
    telegram_id: int,
) -> bool:
    result = await session.execute(
        delete(
            BlacklistUserModel,
        ).where(
            BlacklistUserModel.user_telegram_id == telegram_id,
        ),
    )
    await session.commit()

    await log_add_event(
        session,
        event_type=LogEventType.USER_WAS_REMOVED_FROM_BLACKLIST,
        metadata={"user_telegram_id": telegram_id},
    )

    return bool(result.rowcount)


async def get_blacklist(
    session: AsyncSession,
    count: int,
) -> list[BlacklistUserModel]:
    return list(
        await session.scalars(
            select(
                BlacklistUserModel,
            )
            .order_by(
                BlacklistUserModel.id,
            )
            .limit(count),
        )
    )


def is_admin(telegram_id: int) -> bool:
    return telegram_id == ADMIN_ID


__all__ = [
    "is_in_blacklist",
    "add_to_blacklist",
    "remove_from_blacklist",
    "is_admin",
]
