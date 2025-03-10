import os
from collections.abc import AsyncGenerator

from database import AsyncSessionFactory
from sqlalchemy.ext.asyncio import AsyncSession




async def async_get_db() -> AsyncGenerator[AsyncSession, Exception]:
    async with AsyncSessionFactory() as session:
        try:
            yield session
        except Exception as e:
            print(f"An error occurred: {e}")
            raise e
