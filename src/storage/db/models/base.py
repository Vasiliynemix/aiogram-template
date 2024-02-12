from datetime import datetime

from sqlalchemy import Integer, DateTime, func
from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column


class Base(DeclarativeBase):
    @classmethod
    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    __allow_unmapped__ = False

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(), nullable=True, onupdate=func.now()
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(), nullable=False, server_default=func.now()
    )
