from .base import Base
from .mixins import IDMixin, AuthorTelegramIDMixin


class BlacklistUserAddedLogModel(Base, IDMixin, AuthorTelegramIDMixin):
    __tablename__ = "blacklist_user_added_logs"


__all__ = [
    "BlacklistUserAddedLogModel",
]
