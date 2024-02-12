from collections.abc import Awaitable, Callable
from typing import Any

from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery, Message

from src.storage.db.db import Database
from src.storage.storage import Storage


class StorageMiddleware(BaseMiddleware):
    def __init__(self, storage: Storage) -> None:
        self.storage = storage

    async def __call__(
        self,
        handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
        event: Message | CallbackQuery,
        data: dict[str, Any],
    ) -> Any:
        async with self.storage.db.async_session() as session:
            data["db"]: Database = Database(session)
            user = await data["db"].user.get(event.from_user.id)
            data["user"] = user
            return await handler(event, data)
