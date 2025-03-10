from pydantic import BaseModel, EmailStr, Field


class UserPatch(BaseModel):
    fio: str = Field(max_length=30, default=None)
    course: str = Field(max_length=1, default=None)
    group: EmailStr = Field(max_length=2, default=None)
    direction: str = Field(max_length=20, default=None)
