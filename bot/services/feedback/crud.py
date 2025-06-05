from sqlalchemy import select, update

from ...core.database import sessionmaker
from ...core.system_logger import async_system_logger_decorator
from ...core.models import FeedbackModel


@async_system_logger_decorator()
async def send_feedback(
    message: str,
    rate: int,
    will_he_buy_more: bool,
    author_telegram_id: int,
) -> bool:
    async with sessionmaker() as session:
        if (
            await session.execute(
                select(
                    FeedbackModel,
                ).where(
                    FeedbackModel.author_telegram_id == author_telegram_id,
                ),
            )
        ).scalar_one_or_none():
            result = await session.execute(
                update(
                    FeedbackModel,
                )
                .values(
                    content=message,
                )
                .where(
                    FeedbackModel.author_telegram_id == author_telegram_id,
                ),
            )
            return bool(result.rowcount)
        else:
            session.add(
                FeedbackModel(
                    message=message,
                    rate=rate,
                    will_he_buy_more=will_he_buy_more,
                    author_telegram_id=author_telegram_id,
                )
            )
            await session.commit()
            return True


__all__ = [
    "send_feedback",
]
