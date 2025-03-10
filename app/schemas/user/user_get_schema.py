from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr


class UserGet(BaseModel):
    id: UUID

    fio: str
    course: str
    group: EmailStr
    direction: str

    class Config:
        from_attributes = True
