from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.company.repository import CompanyRepository
from app.domain.company.schema import (
    CompanyCreateSchema,
    CompanyUpdateSchema,
    CompanyOutSchema
)
from app.core.logger import get_logger


logger = get_logger(__name__)


class CompanyService:
    """Service layer for company business logic."""
    
    def __init__(self, repo: CompanyRepository):
        self.repo = repo

    async def get_all(self, db: AsyncSession) -> list[CompanyOutSchema]:
        """Retrieve all companies."""
        return await self.repo.get_all(db)

    async def get_by_id(self, db: AsyncSession, company_id: int) -> CompanyOutSchema | None:
        """Retrieve company by ID."""
        return await self.repo.get_by_id(db, company_id)

    async def create(self, db: AsyncSession, company_data: CompanyCreateSchema) -> CompanyOutSchema:
        """Create a new company."""
        return await self.repo.create(db, company_data)

    async def update(
        self, 
        db: AsyncSession,
        company_id: int, 
        company_data: CompanyUpdateSchema
    ) -> CompanyOutSchema:
        """Update existing company."""
        return await self.repo.update(db, company_id, company_data)

    async def delete_by_id(self, db: AsyncSession, company_id: int) -> None:
        """Delete company by ID."""
        await self.repo.delete_by_id(db, company_id)
