# app/domain/camera/schema.py
from datetime import datetime
from pydantic import field_serializer
from app.common.schema import CamelModel


class CameraCreateSchema(CamelModel):
    """
    Schema for creating a new camera.
    """
    # Basic Info
    name: str
    company_id: int
    
    # Camera Connection
    login: str | None = None
    password: str | None = None
    url: str | None = None
    camera_guid: str | None = None
    
    # Provider Configuration
    type: str
    provider_config: dict | None = None
    provider_mode: str
    provider_image_folder: str | None = None
    
    # Scheduling
    provider_cron_scheme: str | None = None
    collection_interval: str | None = None
    screenshot_interval: int | None = None
    
    # Analysis Configuration
    crop_zones: dict | None = None
    reference_image_url: str | None = None
    kpi_threshold: float | None = None
    
    # Notifications
    notification_chat_id: str | None = None
    
    # Retry Logic
    retry_count: int = 3
    retry_timeout: int = 5
    
    # Status
    is_active: bool = True


class CameraUpdateSchema(CamelModel):
    """
    Schema for updating a camera.
    """
    name: str | None = None
    login: str | None = None
    password: str | None = None
    url: str | None = None
    camera_guid: str | None = None
    type: str | None = None
    provider_config: dict | None = None
    provider_mode: str | None = None
    provider_image_folder: str | None = None
    provider_cron_scheme: str | None = None
    collection_interval: str | None = None
    screenshot_interval: int | None = None
    crop_zones: dict | None = None
    reference_image_url: str | None = None
    kpi_threshold: float | None = None
    notification_chat_id: str | None = None
    retry_count: int | None = None
    retry_timeout: int | None = None
    is_active: bool | None = None


class CameraOutSchema(CamelModel):
    """
    Schema for returning camera details.
    """
    id: int
    name: str
    company_id: int
    login: str | None
    password: str | None
    url: str | None
    camera_guid: str | None
    type: str
    provider_config: dict | None
    provider_mode: str
    provider_image_folder: str | None
    provider_cron_scheme: str | None
    collection_interval: str | None
    screenshot_interval: int | None
    crop_zones: dict | None
    reference_image_url: str | None
    kpi_threshold: float | None
    notification_chat_id: str | None
    retry_count: int
    retry_timeout: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    @field_serializer('created_at', 'updated_at')
    def serialize_datetime(self, dt: datetime) -> str:
        return dt.isoformat()
