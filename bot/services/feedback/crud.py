from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime
from aiogram import Bot

from ...core.locales import get_locale_value
from ...core.models import FeedbackModel
from ...core.configs.bot_config import ADMIN_ID, BOT_TZ


async def send_feedback(
    session: AsyncSession,
    message: str,
    rate: int,
    will_he_buy_more: bool,
    author_telegram_id: int,
    bot: Bot,
):
    if feedback_object := (
        await session.execute(
            select(
                FeedbackModel,
            ).where(
                FeedbackModel.author_telegram_id == author_telegram_id,
            ),
        )
    ).scalar_one_or_none():
        feedback_object.message = message
        feedback_object.created_at = datetime.now(BOT_TZ)
        feedback_object.rate = rate
        feedback_object.will_he_buy_more = will_he_buy_more

    else:
        feedback_object = FeedbackModel(
            message=message,
            rate=rate,
            will_he_buy_more=will_he_buy_more,
            author_telegram_id=author_telegram_id,
        )
        session.add(feedback_object)

    await session.commit()

    await bot.send_message(
        ADMIN_ID,
        get_locale_value("NEW_FEEDBACK_ADMIN_ANNOUNCEMENT", "ru").format(
            feedback_object.author_telegram_id,
            feedback_object.id,
            feedback_object.rate,
            feedback_object.message,
        ),
    )


__all__ = [
    "send_feedback",
]
