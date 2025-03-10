from typing import Annotated
from uuid import UUID

from constants.urls import Urls
from fastapi import APIRouter, Depends, Path, Body
from routers.user_service import UserService
from routers.response_schemas.user_responses import (
    user_create_responses,
    user_find_responses,
    user_edit_responses,
    user_delete_responses,
    user_filter_responses,
)
from schemas.user.user_create_schema import UserCreate
from schemas.user.user_get_schema import UserGet
from schemas.user.user_patch_schema import UserPatch

user_router = APIRouter()

@user_router.post(Urls.add_user.value, response_model=UserGet, responses=user_create_responses)
async def AddUser(
    User_data: Annotated[UserCreate, Body()], user_service: UserService = Depends(UserService)
) -> UserGet:
    return await user_service.create(User_data)

@user_router.get(Urls.finduser.value, response_model=UserGet, responses=user_find_responses)
async def FindUser(
    fio: str, user_service: UserService = Depends(UserService)
) -> UserGet:
    return await user_service.detail(fio)

@user_router.patch(Urls.edit_user.value, response_model=UserGet, responses=user_edit_responses)
async def EditUser(
    fio: str, 
    User_data: Annotated[UserPatch, Body()], 
    user_service: UserService = Depends(UserService)
) -> UserGet:
    return await user_service.patch(fio, User_data)

@user_router.delete(Urls.delete_user.value, responses=user_delete_responses)
async def DeleteUser(
    id: UUID, user_service: UserService = Depends(UserService)
):
    return await user_service.User_delete(id)

@user_router.get(Urls.filter_group.value, response_model=UserGet, responses=user_filter_responses)
async def FilterGroupUser(
    data: str, user_service: UserService = Depends(UserService)
) -> UserGet:
    return await user_service.FilterUserByGroup(data)

@user_router.get(Urls.filter_course.value, response_model=UserGet, responses=user_filter_responses)
async def FilterCourseUser(
    data: str, user_service: UserService = Depends(UserService)
) -> UserGet:
    return await user_service.FilterUserByCourse(data)

@user_router.get(Urls.filter_direction.value, response_model=UserGet, responses=user_filter_responses)
async def FilterDirectionUser(
    data: str, user_service: UserService = Depends(UserService)
) -> UserGet:
    return await user_service.FilterUserByDirection(data)
