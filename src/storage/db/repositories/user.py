from loguru import logger
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.storage.db.models import User


class UserRepo:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def set(self, user_id: int) -> None:
        await self.session.merge(User(user_id=user_id))
        await self.session.commit()
        logger.info("User added to DB")

    async def get(self, user_id: int) -> User | None:
        stmt = select(User).where(User.user_id == user_id)
        return await self.session.scalar(stmt)
