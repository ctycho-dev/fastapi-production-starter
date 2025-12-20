from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.exceptions.exceptions import DatabaseError
from app.common.base_repository import BaseRepository
from app.domain.camera.model import Camera
from app.domain.camera.schema import (
    CameraCreateSchema,
    CameraOutSchema,
)


class CameraRepository(BaseRepository[Camera, CameraOutSchema, CameraCreateSchema]):
    """
    PostgreSQL repository implementation for managing Camera entities.

    This class extends BaseRepository to provide CRUD operations and 
    custom queries for the Camera table.
    """

    def __init__(self):
        """
        Initializes the CameraRepository with the Camera model and related schemas.
        """
        super().__init__(Camera, CameraOutSchema, CameraCreateSchema)
