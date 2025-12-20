# app/domain/camera/service.py
from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.camera.repository import CameraRepository
from app.domain.camera.schema import (
    CameraCreateSchema,
    CameraUpdateSchema,
    CameraOutSchema
)
from app.core.logger import get_logger

logger = get_logger(__name__)


class CameraService:
    """Service layer for camera business logic."""
    
    def __init__(self, repo: CameraRepository):
        self.repo = repo

    async def get_all(self, db: AsyncSession) -> list[CameraOutSchema]:
        """Retrieve all cameras."""
        return await self.repo.get_all(db)

    async def get_by_id(self, db: AsyncSession, camera_id: int) -> CameraOutSchema | None:
        """Retrieve camera by ID."""
        return await self.repo.get_by_id(db, camera_id)

    async def create(self, db: AsyncSession, camera_data: CameraCreateSchema) -> CameraOutSchema:
        """Create a new camera."""
        return await self.repo.create(db, camera_data)

    async def update(
        self, 
        db: AsyncSession,
        camera_id: int, 
        camera_data: CameraUpdateSchema
    ) -> CameraOutSchema | None:
        """Update existing camera."""
        return await self.repo.update(db, camera_id, camera_data)

    async def delete_by_id(self, db: AsyncSession, camera_id: int) -> None:
        """Delete camera by ID."""
        await self.repo.delete_by_id(db, camera_id)
