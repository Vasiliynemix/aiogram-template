from datetime import datetime
from typing import Any, Callable, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery, Message
from loguru import logger


class LoggerMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
        event: Message | CallbackQuery,
        data: dict[str, Any],
    ) -> Any:
        time_start = datetime.now()
        text, type_text = await self.get_text(event)
        try:
            return await handler(event, data)
        except Exception as e:
            logger.error(e)
        finally:
            time_end = datetime.now()
            execution_time = (time_end - time_start).total_seconds() * 1000
            logger.info(
                f"UPDATE -> Duration: {execution_time:.2f} MS | ID: {event.from_user.id} | {type_text}: {text}",
            )

    @staticmethod
    async def get_text(event: Message | CallbackQuery) -> (str, str):
        if isinstance(event, Message):
            return event.text, "Text"
        elif isinstance(event, CallbackQuery):
            return event.data, "Data"
