from .base import Base
from .mixins import IDMixin, TelegramIDMixin


class BlacklistUserAddedLogModel(Base, IDMixin, TelegramIDMixin):
    __tablename__ = "blacklist_user_added_logs"


__all__ = [
    "BlacklistUserAddedLogModel",
]
