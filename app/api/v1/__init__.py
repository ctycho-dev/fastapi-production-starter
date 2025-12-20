from fastapi import APIRouter

from app.core.config import settings

from .camera import router as camera_router
from .report import router as report_router
from .notification import router as notification_router
from .company import router as company_router
from .user import router as user_router

router = APIRouter(
    prefix=settings.api.v1.prefix,
)

router.include_router(camera_router)
router.include_router(report_router)
router.include_router(notification_router)
router.include_router(company_router)
router.include_router(user_router)

__all__ = ["router"]
