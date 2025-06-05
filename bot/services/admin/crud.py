from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from ...core.database import sessionmaker
from ...core.models import BlacklistUserModel
from ...core.configs.bot_config import ADMIN_ID


async def is_in_blacklist(
    session: AsyncSession,
    telegram_id: int,
) -> BlacklistUserModel | None:
    result = (
        await session.execute(
            select(
                BlacklistUserModel,
            ).where(
                BlacklistUserModel.user_telegram_id == telegram_id,
            )
        )
    ).scalar_one_or_none()

    return result


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

    return bool(result.rowcount)


def is_admin(telegram_id: int) -> bool:
    return telegram_id == ADMIN_ID


__all__ = [
    "is_in_blacklist",
    "add_to_blacklist",
    "remove_from_blacklist",
    "is_admin",
]
