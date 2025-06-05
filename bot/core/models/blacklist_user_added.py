from .base import Base
from .mixins import IDMixin, UserTelegramIDMixin


class BlacklistUserAddedLogModel(Base, IDMixin, UserTelegramIDMixin):
    __tablename__ = "blacklist_user_added_logs"


__all__ = [
    "BlacklistUserAddedLogModel",
]
