# app/api/v1/camera.py
from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.camera.schema import (
    CameraCreateSchema,
    CameraUpdateSchema,
    CameraOutSchema
)
from app.domain.camera.service import CameraService
from app.api.dependencies import get_db, get_camera_service
from app.core.logger import get_logger
from app.core.config import settings
from app.middleware.rate_limiter import limiter

logger = get_logger(__name__)

router = APIRouter(prefix=settings.api.v1.camera, tags=["Camera"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CameraOutSchema)
@limiter.limit("20/minute")
async def create_camera(
    request: Request,
    camera: CameraCreateSchema,
    db: AsyncSession = Depends(get_db),
    service: CameraService = Depends(get_camera_service)
):
    """Create a new camera."""
    created_camera = await service.create(db, camera)
    return created_camera


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[CameraOutSchema])
@limiter.limit("60/minute")
async def get_all_cameras(
    request: Request,
    db: AsyncSession = Depends(get_db),
    service: CameraService = Depends(get_camera_service)
):
    """Retrieve all cameras."""
    cameras = await service.get_all(db)
    return cameras


@router.get("/{camera_id}", status_code=status.HTTP_200_OK, response_model=CameraOutSchema)
@limiter.limit("100/minute")
async def get_camera_by_id(
    request: Request,
    camera_id: int,
    db: AsyncSession = Depends(get_db),
    service: CameraService = Depends(get_camera_service)
):
    """Retrieve a single camera by ID."""
    camera = await service.get_by_id(db, camera_id)
    return camera


@router.put("/{camera_id}", status_code=status.HTTP_200_OK, response_model=CameraOutSchema)
@limiter.limit("20/minute")
async def update_camera(
    request: Request,
    camera_id: int,
    camera_data: CameraUpdateSchema,
    db: AsyncSession = Depends(get_db),
    service: CameraService = Depends(get_camera_service)
):
    """Update existing camera."""
    updated_camera = await service.update(db, camera_id, camera_data)
    return updated_camera


@router.delete("/{camera_id}", status_code=status.HTTP_204_NO_CONTENT)
@limiter.limit("20/minute")
async def delete_camera_by_id(
    request: Request,
    camera_id: int,
    db: AsyncSession = Depends(get_db),
    service: CameraService = Depends(get_camera_service)
):
    """Delete a camera by ID."""
    await service.delete_by_id(db, camera_id)
    