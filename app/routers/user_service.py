from json import dumps
from typing import Callable
from uuid import UUID

from crud.user.user import (
    GetUserByFIO,
    DeleteUser,
    CreateUser,
    UpdateUser,
    FilterUserByGroup,
    FilterUserByCourse,
    FilterUserByDirection,
)
from dependecies import async_get_db
from fastapi import Depends
from models.User import User
from schemas.user.user_create_schema import UserCreate
from schemas.user.user_get_schema import UserGet
from schemas.user.user_patch_schema import UserPatch
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm.decl_api import DeclarativeMeta
from sqlalchemy.sql.selectable import Select


class UserService(
):

    model: DeclarativeMeta = User
    schema: UserGet = UserGet
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

    async def detail(self, fio: str) -> UserGet:

        User: User | None = await GetUserByFIO(self.db, fio=fio)
        return UserGet.model_validate(User)


    async def create(self, User_data: UserCreate) -> UserGet:
        """
        Creates a new User in the database using the provided data.

        Parameters:
        User_data (UserCreate): A dictionary containing the data for the new User.

        Returns:
        UserGet: A dictionary representing the newly created User, validated according to the UserGet schema.
        """
        User: User = await CreateUser(self.db, User_data)
        return UserGet.model_validate(User)

    async def patch(self, fio: str, User_data: UserPatch) -> UserGet:
        """
        Updates an existing User in the database with the provided data.

        Parameters:
        User_id (UUID): The unique identifier of the User to update.
        User_data (UserPatch): A dictionary containing the updated data for the User.
            The dictionary should only include the fields that need to be updated.

        Returns:
        UserGet: A dictionary representing the updated User, validated according to the UserGet schema.
            The returned dictionary contains the updated User's data.
        """
        User_to_patch: User | None = await GetUserByFIO(self.db, fio=fio)
        patched_User: User = await UpdateUser(self.db, User_to_patch, User_data)
        return UserGet.model_validate(patched_User)
        """
        Deletes a User from the database using the provided User ID.

        Parameters:
        User_id (UUID): The unique identifier of the User to delete.

        Returns:
        None: The function does not return any value. It deletes the User from the database.

        Raises:
        Exception: If the User with the provided User_id is not found in the database.
        """

    async def User_delete(self, User_id: UUID):
        return await DeleteUser(self.db, User_id)

    async def User_filter_group(self, User_data: str):
        return await FilterUserByGroup(self.db, User_data)

    async def User_filter_course(self, User_data: str):
        return await FilterUserByCourse(self.db, User_data)

    async def User_filter_direction(self, User_data: str):
        return await FilterUserByDirection(self.db, User_data)
