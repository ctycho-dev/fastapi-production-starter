from fastapi import APIRouter, Depends, Request, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.middleware.rate_limiter import limiter
from app.api.dependencies import get_company_service, get_db
from app.domain.company.service import CompanyService
from app.domain.company.schema import (
    CompanyCreateSchema,
    CompanyUpdateSchema,
    CompanyOutSchema
)
from app.core.logger import get_logger
from app.core.config import settings


logger = get_logger(__name__)
router = APIRouter(prefix=settings.api.v1.company, tags=["Company"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CompanyOutSchema)
@limiter.limit("10/minute")
async def create_company(
    request: Request,
    payload: CompanyCreateSchema,
    db: AsyncSession = Depends(get_db),
    service: CompanyService = Depends(get_company_service)
):
    """Create a new company."""
    return await service.create(db, payload)


@router.get("/", response_model=list[CompanyOutSchema])
@limiter.limit("60/minute")
async def get_companies(
    request: Request,
    db: AsyncSession = Depends(get_db),
    service: CompanyService = Depends(get_company_service)
):
    """Retrieve all companies."""
    return await service.get_all(db)


@router.get("/{company_id}", response_model=CompanyOutSchema)
@limiter.limit("100/minute")
async def get_company(
    request: Request,
    company_id: int,
    db: AsyncSession = Depends(get_db),
    service: CompanyService = Depends(get_company_service)
):
    """Retrieve company by ID."""
    return await service.get_by_id(db, company_id)


@router.put("/{company_id}", response_model=CompanyOutSchema)
@limiter.limit("30/minute")
async def update_company(
    request: Request,
    company_id: int,
    payload: CompanyUpdateSchema,
    db: AsyncSession = Depends(get_db),
    service: CompanyService = Depends(get_company_service)
):
    """Update company by ID."""
    return await service.update(db, company_id, payload)


@router.delete("/{company_id}", status_code=status.HTTP_204_NO_CONTENT)
@limiter.limit("10/minute")
async def delete_company(
    request: Request,
    company_id: int,
    db: AsyncSession = Depends(get_db),
    service: CompanyService = Depends(get_company_service)
):
    """Delete company by ID."""
    await service.delete_by_id(db, company_id)
