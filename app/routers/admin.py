from typing import Annotated
from uuid import UUID

from constants.urls import Urls
from fastapi import APIRouter, Body, Depends, HTTPException, Path
from routers.admin_service import AdminService
from routers.response_schemas.admin_responses import (
    admin_create_responses,
    admin_detail_responses,
)
from schemas.admin.admin_create_schema import AdminCreate
from schemas.admin.admin_get_schema import AdminGet

admin_router = APIRouter()

@admin_router.get(Urls.add_admin.value, response_model = AdminGet, responses = admin_create_responses)
async def AddAdmin(data: Annotated[AdminCreate, Body()], admin_service: AdminService = Depends(AdminService)) -> AdminGet:
    return await admin_service.create(data)

@admin_router.get(Urls.admin_check.value, response_model = AdminGet, responses = admin_create_responses)
async def CheckAdmin(data: str, admin_service: AdminService = Depends(AdminService)) -> AdminGet:
    return await admin_service.detail(data)