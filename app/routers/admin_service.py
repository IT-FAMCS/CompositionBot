from json import dumps
from typing import Callable
from uuid import UUID

from crud.admin.admin import (
    CheckAdmin,
    AddAdmin,
)
from dependecies import async_get_db
from fastapi import Depends
from models.Admin import Admin
from schemas.admin.admin_create_schema import AdminCreate
from schemas.admin.admin_get_schema import AdminGet
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm.decl_api import DeclarativeMeta
from sqlalchemy.sql.selectable import Select


class AdminService(
):

    model: DeclarativeMeta = Admin
    schema: AdminGet = AdminGet
    fileds_to_search: list[str] = ["first_name", "last_name", "title", "company"]

    def _get_query(self, *args, **kwargs) -> Select:
        """
        Constructs a SQLAlchemy Select query for the User model, optionally filtering
        by search fields and User statuses.

        Parameters:
        *args: Additional positional arguments.
        **kwargs: Additional keyword arguments.
            - template (str): A search string to filter Users by specific fields.
            - statuses (list[str]): A list of User statuses to filter the query.

        Returns:
        Select: A SQLAlchemy Select object representing the constructed query.
        """
        teamplate: str = kwargs.get("template", "")



    def __init__(self, db: AsyncSession = Depends(async_get_db)):
        self.db: AsyncSession = db

    """
    Retrieves a single User by its ID from the database and returns it as a dictionary
    validated according to the UserGet schema.

    Parameters:
    User_id (UUID): The unique identifier of the User to retrieve.

    Returns:
    UserGet: A dictionary representing the retrieved User, validated according to the UserGet schema.
    """

    async def detail(self, data: str) -> AdminGet:

        Admin: Admin | None = await CheckAdmin(self.db, data=data)
        return AdminGet.model_validate(User)


    async def create(self, data: AdminCreate) -> AdminGet:
        """
        Creates a new User in the database using the provided data.

        Parameters:
        User_data (UserCreate): A dictionary containing the data for the new User.

        Returns:
        UserGet: A dictionary representing the newly created User, validated according to the UserGet schema.
        """
        Admin: Admin = await AddAdmin(self.db, data)
        return AdminGet.model_validate(User)

    