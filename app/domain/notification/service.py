from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.notification.repository import NotificationRepository
from app.domain.notification.schema import (
    NotificationCreateSchema,
    NotificationOutSchema
)
from app.core.logger import get_logger

logger = get_logger(__name__)


class NotificationService:
    """Service layer for notification business logic."""
    
    def __init__(self, repo: NotificationRepository):
        self.repo = repo

    async def get_all(self, db: AsyncSession) -> list[NotificationOutSchema]:
        """Retrieve all notifications."""
        return await self.repo.get_all(db)

    async def get_by_id(self, db: AsyncSession, notification_id: int) -> NotificationOutSchema | None:
        """Retrieve notification by ID."""
        return await self.repo.get_by_id(db, notification_id)

    async def create(self, db: AsyncSession, notification_data: NotificationCreateSchema) -> NotificationOutSchema:
        """Create a new notification."""
        return await self.repo.create(db, notification_data)

    async def delete_by_id(self, db: AsyncSession, notification_id: int) -> None:
        """Delete notification by ID."""
        await self.repo.delete_by_id(db, notification_id)
