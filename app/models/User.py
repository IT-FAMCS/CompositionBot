from uuid import uuid4

from models import Base
from sqlalchemy import UUID, Column, String, Text, Boolean


class User(Base):
    __tablename__ = "tbl_user"

    id = Column(UUID, primary_key=True, nullable=False, unique=True, default=uuid4())
    fio = Column(String(30), unique=True)
    course = Column(String(1))
    group = Column(String(2))
    direction = Column(String(20))
