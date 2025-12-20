from app.common.base_repository import BaseRepository
from app.domain.notification.model import Notification
from app.domain.notification.schema import (
    NotificationCreateSchema,
    NotificationOutSchema
)


class NotificationRepository(BaseRepository[Notification, NotificationOutSchema, NotificationCreateSchema]):
    """
    PostgreSQL repository implementation for managing Notification entities.

    This class extends BaseRepository to provide CRUD operations and 
    custom queries for the Notification table.
    """

    def __init__(self):
        """
        Initializes the NotificationRepository with the Notification model and related schemas.
        """
        super().__init__(Notification, NotificationOutSchema, NotificationCreateSchema)
