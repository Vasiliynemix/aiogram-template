from typing import Any

from sqlalchemy import URL
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)

from src.config import Config


class DBConnect:
    LEVEL = Config().log_level

    def __init__(self, url: str | URL) -> None:
        self.url = url
        self.level = self.LEVEL
        self.engine = self.__set_engine()

    @property
    def async_session(self):
        return self.__async_session_factory(bind=self.engine)

    def __set_engine(self) -> AsyncEngine:
        if self.level != "debug":
            self.level = None
        return create_async_engine(url=self.url, echo=self.level, pool_pre_ping=True)

    @staticmethod
    def __async_session_factory(bind: Any) -> AsyncSession | Any:
        return async_sessionmaker(
            bind=bind, class_=AsyncSession, expire_on_commit=False
        )
