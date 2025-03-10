import logging
from datetime import datetime
from uuid import UUID

from base.decorators.transaction import async_transaction
from models.User import User
from schemas.user.user_create_schema import UserCreate
from schemas.user.user_patch_schema import UserPatch
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.selectable import Select

logger = logging.getLogger(__name__)


@async_transaction
async def GetUserByFIO(db: AsyncSession, fio: str) -> User | None:
    query: Select = select(User).where(User.fio == user_fio)
    result = await db.execute(query)
    user: User | None = result.scalar_one_or_none()
    return user

@async_transaction
async def DeleteUser(db: AsyncSession, data: UUID):
    query: Select = select(User).where(User.id == data)
    result = db.execute(query)
    user: User | None = result.scalar_one_or_none()
    if user in None:
        logging.warning(f"User with ID {data} not found.")
        return F"Участник с ID {data} не найден."
    await db.delete(user)
    await db.commit()
    return f"Удален участник с ID {data}."

@async_transaction
async def CreateUser(db: AsyncSession, data: UserCreate) -> User | None:
    user_data_dict = data.model_dump()

    user: User = User(**user_data_dict)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

@async_transaction
async def UpdateUser(db: AsyncSession, user_to_update: User, data: UserPatch) -> User | None:
    user_data_dict = data.model_dump(exclude_unset=True)

    for key, value in user_data_dict.items():
        if value is not None:
            setattr(user_to_update, key, value)

    db.add(user_to_update)
    await db.commit()
    await db.refresh(user_to_update)
    return user_to_update

@async_transaction
async def FilterUserByGroup(db: AsyncSession, data: str) -> list | None:
    query: Select = select(User).where(User.group == data)
    result = await db.execute(query)
    users: list | None = result
    return users

@async_transaction
async def FilterUserByCourse(db: AsyncSession, data: str) -> list | None:
    query: Select = select(User).where(User.course == course)
    result = await db.execute(query)
    users: list | None = result
    return users

@async_transaction
async def FilterUserByDirection(db: AsyncSession, data: str) -> list | None:
    query: Select = select(User).where(User.direction == direction)
    result = await db.execute(query)
    users: list | None = result
    return users