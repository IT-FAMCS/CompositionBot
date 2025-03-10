from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr


class AdminGet(BaseModel):
    id: UUID

    username: str



