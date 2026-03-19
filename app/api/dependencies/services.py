import httpx
from fastapi import (
    HTTPException,
    status,
    Request,
    Depends
)
import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from jose import JWTError
from app.domain.user.schema import UserOutSchema
from app.domain.camera.repository import CameraRepository
from app.domain.company.repository import CompanyRepository
from app.domain.user.repository import UserRepository
from app.domain.notification.repository import NotificationRepository
from app.domain.report.repository import ReportRepository
from app.domain.camera.repository import CameraRepository
from app.domain.camera.service import CameraService
from app.domain.report.service import ReportService
from app.domain.user.service import UserService
from app.domain.camera.service import CameraService
from app.domain.company.service import CompanyService
from app.domain.notification.service import NotificationService
from app.enums.enums import UserRole
from app.core.config import settings
from app.database.connection import db_manager
from app.middleware.logging import set_user_email
from app.utils.oauth2 import verify_access_token



# -------------------------
# Repository Factories
# -------------------------


def get_camera_repo() -> CameraRepository:
    return CameraRepository()


def get_company_repo() -> CompanyRepository:
    return CompanyRepository()


def get_user_repo() -> UserRepository:
    return UserRepository()


def get_notification_repo() -> NotificationRepository:
    return NotificationRepository()


def get_report_repo() -> ReportRepository:
    """Provide report repository instance."""
    return ReportRepository()


def get_camera_repo() -> CameraRepository:
    """Provide camera repository instance."""
    return CameraRepository()


# -------------------------
# Services
# -------------------------
def get_user_service(
    repo: UserRepository = Depends(get_user_repo),
) -> UserService:

    return UserService(repo=repo)


def get_camera_service(
    db: AsyncSession = Depends(get_db),
    repo: CameraRepository = Depends(get_camera_repo),
) -> CameraService:

    return CameraService(db=db, repo=repo)


def get_company_service(
    repo: CompanyRepository = Depends(get_company_repo),
) -> CompanyService:

    return CompanyService(repo=repo)


def get_notification_service(
    db: AsyncSession = Depends(get_db),
    repo: CompanyRepository = Depends(get_notification_repo),
) -> NotificationService:
    return NotificationService(repo=repo)


def get_report_service(
    repo: ReportRepository = Depends(get_report_repo)
) -> ReportService:
    """Provide report service instance."""
    return ReportService(repo=repo)


def get_camera_service(
    repo: CameraRepository = Depends(get_camera_repo)
) -> CameraService:
    """Provide camera service instance."""
    return CameraService(repo=repo)