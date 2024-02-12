from aiogram import Dispatcher

from src.bot.middlewares.logger_mw import LoggerMiddleware
from src.bot.middlewares.storage_mw import StorageMiddleware
from src.storage.storage import Storage


class TGBotMiddleware:
    def __init__(self, storage: Storage) -> None:
        self.storage = storage

    def setup(self, dp: Dispatcher) -> None:
        dp.message.outer_middleware(StorageMiddleware(storage=self.storage))
        dp.callback_query.outer_middleware(StorageMiddleware(storage=self.storage))

        dp.message.middleware(LoggerMiddleware())
        dp.callback_query.middleware(LoggerMiddleware())
