from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Request,
    status,
)
from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.notification.schema import (
    NotificationCreateSchema,
    NotificationOutSchema
)
from app.domain.notification.service import NotificationService
from app.api.dependencies import get_db, get_notification_service
from app.core.logger import get_logger
from app.core.config import settings
from app.middleware.rate_limiter import limiter

logger = get_logger(__name__)

router = APIRouter(prefix=settings.api.v1.notification, tags=["Notification"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=NotificationOutSchema)
@limiter.limit("20/minute")
async def create_notification(
    request: Request,
    notification: NotificationCreateSchema,
    db: AsyncSession = Depends(get_db),
    service: NotificationService = Depends(get_notification_service)
):
    """Create a new notification."""
    created_notification = await service.create(db, notification)
    return created_notification


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[NotificationOutSchema])
@limiter.limit("60/minute")
async def get_all_notifications(
    request: Request,
    db: AsyncSession = Depends(get_db),
    service: NotificationService = Depends(get_notification_service)
):
    """Retrieve all notifications."""
    notifications = await service.get_all(db)
    return notifications


@router.get("/{notification_id}", status_code=status.HTTP_200_OK, response_model=NotificationOutSchema)
@limiter.limit("100/minute")
async def get_notification_by_id(
    request: Request,
    notification_id: int,
    db: AsyncSession = Depends(get_db),
    service: NotificationService = Depends(get_notification_service)
):
    """Retrieve a single notification by ID."""
    notification = await service.get_by_id(db, notification_id)
    return notification


@router.delete("/{notification_id}", status_code=status.HTTP_204_NO_CONTENT)
@limiter.limit("20/minute")
async def delete_notification_by_id(
    request: Request,
    notification_id: int,
    db: AsyncSession = Depends(get_db),
    service: NotificationService = Depends(get_notification_service)
):
    """Delete a notification by ID."""
    await service.delete_by_id(db, notification_id)
