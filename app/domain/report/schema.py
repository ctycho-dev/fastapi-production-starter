# app/domain/report/schema.py
from datetime import datetime
from pydantic import field_serializer
from app.common.schema import CamelModel


class ReportCreateSchema(CamelModel):
    """
    Schema for creating a new report.

    Attributes:
        camera_id (int): Foreign key to the camera.
        fill_percentage (float | None): The fill percentage value.
        compliance_percentage (float | None): The compliance percentage value.
        screenshot_s3_url (str | None): S3 URL for the screenshot.
        analysis_text (str | None): Analysis text description.
    """
    camera_id: int
    fill_percentage: float | None = None
    compliance_percentage: float | None = None
    screenshot_s3_url: str | None = None
    analysis_text: str | None = None


class ReportUpdateSchema(CamelModel):
    """
    Schema for updating a report.

    Attributes:
        fill_percentage (float | None): The fill percentage value.
        compliance_percentage (float | None): The compliance percentage value.
        screenshot_s3_url (str | None): S3 URL for the screenshot.
        analysis_text (str | None): Analysis text description.
    """
    fill_percentage: float | None = None
    compliance_percentage: float | None = None
    screenshot_s3_url: str | None = None
    analysis_text: str | None = None


class ReportOutSchema(CamelModel):
    """
    Schema for returning report details.

    Attributes:
        id (int): Unique identifier of the report.
        camera_id (int): Foreign key to the camera.
        fill_percentage (float | None): The fill percentage value.
        compliance_percentage (float | None): The compliance percentage value.
        screenshot_s3_url (str | None): S3 URL for the screenshot.
        analysis_text (str | None): Analysis text description.
        created_at (datetime): Timestamp of when the report was created.
        updated_at (datetime): Timestamp of when the report was last updated.
    """
    id: int
    camera_id: int
    fill_percentage: float | None
    compliance_percentage: float | None
    screenshot_s3_url: str | None
    analysis_text: str | None
    created_at: datetime
    updated_at: datetime

    @field_serializer('created_at', 'updated_at')
    def serialize_datetime(self, dt: datetime) -> str:
        """
        Serialize datetime fields to ISO 8601 string format.

        Args:
            dt (datetime): The datetime to serialize.

        Returns:
            str: The ISO 8601 formatted datetime string.
        """
        return dt.isoformat()
