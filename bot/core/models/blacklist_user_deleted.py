from .base import Base
from .mixins import IDMixin, AuthorTelegramIDMixin


class BlacklistUserDeletedLogModel(Base, IDMixin, AuthorTelegramIDMixin):
    __tablename__ = "blacklist_user_deleted_logs"


__all__ = [
    "BlacklistUserDeletedLogModel",
]
