from datetime import datetime
from pydantic import ConfigDict, field_serializer
from app.common.schema import CamelModel


class NotificationCreateSchema(CamelModel):
    """
    Schema for creating a new notification.

    Attributes:
        text (str): The notification text/message.
        status (str): The notification status.
        report_id (int): Foreign key to the report.
    """
    text: str
    status: str
    report_id: int | None


class NotificationOutSchema(CamelModel):
    """
    Schema for returning notification details.

    Attributes:
        id (int): Unique identifier of the notification.
        text (str): The notification text/message.
        status (str): The notification status.
        report_id (int): Foreign key to the report.
        created_at (datetime): Timestamp of when the notification was created.
    """
    id: int
    text: str
    status: str
    report_id: int | None
    created_at: datetime

    @field_serializer('created_at')
    def serialize_created_at(self, created_at: datetime) -> str:
        """
        Serialize the `created_at` field to an ISO 8601 string format.

        Args:
            created_at (datetime): The datetime to serialize.

        Returns:
            str: The ISO 8601 formatted datetime string.
        """
        return created_at.isoformat()
