import logging
from datetime import datetime
from uuid import UUID

from base.decorators.transaction import async_transaction
from models.Admin import Admin
from schemas.admin.admin_create_schema import AdminCreate
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.selectable import Select

@async_transaction
async def CheckAdmin(bd: AsyncSession, data: str) -> Admin | None:
    query: Select = select(Admin).where(Admin.username == data)
    result = await db.execute(query)
    admin: Admin | None = result.scalar_one_or_none()
    if admin is not None:
        return True
    else:
        return False
    
@async_transaction
async def AddAdmin(db: AsyncSession, data: AdminCreate) -> Admin | None:
    admin_data_dict = data.model_dump()

    admin: Admin = Admin(**admin_data_dict)
    db.add(admin)
    await db.commit()
    await db.refresh(admin)
    return result