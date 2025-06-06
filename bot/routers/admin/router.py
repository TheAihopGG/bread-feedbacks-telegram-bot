from aiogram import Router, F
from aiogram.filters import Command

from .handlers.admin_panel import admin_panel
from .handlers.add_to_blacklist import (
    add_to_blacklist_get_user_id,
    add_to_blacklist_callback,
)
from .handlers.show_blacklist import show_blacklist_callback, show_blacklist_get_count
from .handlers.remove_from_blacklist import (
    remove_from_blacklist_callback,
    remove_from_blacklist_get_user_id,
)
from .forms import AddToBlacklistForm, RemoveFromBlacklistForm, ShowBlacklistForm
from ...middlewares import AdminFilterMiddleware

router = Router(name="admin")
router.message.middleware.register(AdminFilterMiddleware())

router.message.register(
    admin_panel,
    Command("admin-panel"),
)

router.callback_query.register(
    add_to_blacklist_callback,
    F.data == "add_to_blacklist_callback",
)
router.message.register(
    add_to_blacklist_get_user_id,
    AddToBlacklistForm.user_id,
)

router.callback_query.register(
    show_blacklist_callback,
    F.data == "show_blacklist_callback",
)
router.message.register(
    show_blacklist_get_count,
    ShowBlacklistForm.count,
)

router.callback_query.register(
    remove_from_blacklist_callback,
    F.data == "remove_from_blacklist_callback",
)
router.message.register(
    remove_from_blacklist_get_user_id,
    RemoveFromBlacklistForm.user_id,
)
