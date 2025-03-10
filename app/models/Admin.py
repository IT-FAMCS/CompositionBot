from uuid import uuid4

from models import Base
from sqlalchemy import UUID, Column, String, Text, Boolean


class Admin(Base):
    __tablename__ = "tbl_admin"

    id = Column(UUID, primary_key=True, nullable=False, unique=True, default=uuid4())
    username = Column(String(20), unique=True)