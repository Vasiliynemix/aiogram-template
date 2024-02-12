from sqlalchemy.ext.asyncio import AsyncSession

from src.storage.db.repositories.user import UserRepo


class Database:
    def __init__(
        self,
        session: AsyncSession,
    ):
        self.session = session
        self.user: UserRepo = UserRepo(session)
