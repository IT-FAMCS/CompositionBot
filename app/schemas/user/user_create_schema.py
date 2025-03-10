from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    fio: str = Field(max_length=30)
    course: str = Field(max_length=1)
    group: EmailStr = Field(max_length=2)
    direction: str = Field(max_length=20)
