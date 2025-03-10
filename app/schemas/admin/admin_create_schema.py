from pydantic import BaseModel, EmailStr, Field


class AdminCreate(BaseModel):
    username: str = Field(max_length=20)

