from sqlalchemy import BigInteger
from sqlalchemy.orm import mapped_column, Mapped

from src.storage.db.models.base import Base


class User(Base):
    user_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    first_name: Mapped[str] = mapped_column(nullable=True)
    last_name: Mapped[str] = mapped_column(nullable=True)
    username: Mapped[str] = mapped_column(nullable=True)
