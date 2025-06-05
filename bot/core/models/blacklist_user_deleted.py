from .base import Base
from .mixins import IDMixin, UserTelegramIDMixin


class BlacklistUserDeletedLogModel(Base, IDMixin, UserTelegramIDMixin):
    __tablename__ = "blacklist_user_deleted_logs"


__all__ = [
    "BlacklistUserDeletedLogModel",
]
