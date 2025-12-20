# app/domain/Report/repository.py
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import delete

from app.exceptions.exceptions import DatabaseError
from app.common.base_repository import BaseRepository
from app.domain.report.model import Report
from app.domain.report.schema import (
    ReportCreateSchema,
    ReportOutSchema,
)


class ReportRepository(BaseRepository[Report, ReportOutSchema, ReportCreateSchema]):
    """
    PostgreSQL repository implementation for managing Report entities.

    This class extends BaseRepository to provide CRUD operations and 
    custom queries for the Report table.
    """

    def __init__(self):
        """
        Initializes the ReportRepository with the Report model and related schemas.
        """
        super().__init__(Report, ReportOutSchema, ReportCreateSchema)

    async def get_by_camera_id(self, db: AsyncSession, camera_id: int) -> list[ReportOutSchema]:
        """Retrieve all reports for a specific camera."""
        result = await db.execute(select(Report).where(Report.camera_id == camera_id))
        return list(result.scalars().all())
