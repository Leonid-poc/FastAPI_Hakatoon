from typing import AsyncGenerator

from fastapi import Depends
from sqlalchemy import String, Column, Boolean, VARCHAR, Integer, ForeignKey, TIMESTAMP
from datetime import datetime
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase
from models.models import role

DATABASE_URL = "postgresql+asyncpg://postgres:1234@localhost:5432/Hakaton"


Base: DeclarativeBase = declarative_base()


class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(255), nullable=False)
    phone = Column(VARCHAR(50), nullable=True)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    role_id = Column(Integer, ForeignKey(role.c.id), default=1)

    email: str = Column(VARCHAR(255), unique=True, index=True, nullable=False) # String(length=320)
    hashed_password: str = Column(String, nullable=False) # String(length=1024)
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)


engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)