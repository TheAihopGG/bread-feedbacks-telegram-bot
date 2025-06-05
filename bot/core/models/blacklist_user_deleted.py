from .base import Base
from .mixins import IDMixin, TelegramIDMixin


class BlacklistUserDeletedLogModel(Base, IDMixin, TelegramIDMixin):
    __tablename__ = "blacklist_user_deleted_logs"


__all__ = [
    "BlacklistUserDeletedLogModel",
]
