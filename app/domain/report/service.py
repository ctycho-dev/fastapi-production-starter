from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.report.repository import ReportRepository
from app.domain.report.schema import (
    ReportCreateSchema,
    ReportUpdateSchema,
    ReportOutSchema
)
from app.core.logger import get_logger

logger = get_logger(__name__)


class ReportService:
    """Service layer for report business logic."""
    
    def __init__(self, repo: ReportRepository):
        self.repo = repo

    async def get_all(self, db: AsyncSession) -> list[ReportOutSchema]:
        """Retrieve all reports."""
        return await self.repo.get_all(db)

    async def get_by_id(self, db: AsyncSession, report_id: int) -> ReportOutSchema | None:
        """Retrieve report by ID."""
        return await self.repo.get_by_id(db, report_id)

    async def get_by_camera_id(self, db: AsyncSession, camera_id: int) -> list[ReportOutSchema]:
        """Retrieve all reports for a specific camera."""
        return await self.repo.get_by_camera_id(db, camera_id)

    async def create(self, db: AsyncSession, report_data: ReportCreateSchema) -> ReportOutSchema:
        """Create a new report."""
        return await self.repo.create(db, report_data)

    async def update(
        self, 
        db: AsyncSession,
        report_id: int, 
        report_data: ReportUpdateSchema
    ) -> ReportOutSchema | None:
        """Update existing report."""
        return await self.repo.update(db, report_id, report_data)

    async def delete_by_id(self, db: AsyncSession, report_id: int) -> None:
        """Delete report by ID."""
        await self.repo.delete_by_id(db, report_id)
