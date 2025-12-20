from sqlalchemy import String, Integer, ForeignKey, Boolean, Float
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional
from app.database.connection import Base
from app.common.audit_mixin import UserAuditMixin, TimestampMixin


class Camera(Base, UserAuditMixin, TimestampMixin):
    __tablename__ = "camera"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    # ---- Basic Info ----
    name: Mapped[str] = mapped_column(String, nullable=False)

    company_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("company.id"), nullable=False, index=True
    )
    # ---- Camera Connection ----
    login: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    password: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    url: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    camera_guid: Mapped[Optional[str]] = mapped_column(
        String, nullable=True, index=True
    )

    # ---- Provider Configuration ----
    type: Mapped[str] = mapped_column(
        String, nullable=False, comment="axxon-next, trassir-cloud, trassir-server, etc."
    )
    provider_config: Mapped[Optional[dict]] = mapped_column(
        JSONB, nullable=True, comment="JSONB config for connection and provider script (including recorder version)"
    )
    provider_mode: Mapped[str] = mapped_column(
        String, nullable=False, comment="single or stream"
    )
    provider_image_folder: Mapped[Optional[str]] = mapped_column(
        String, nullable=True, comment="Folder name for storing images"
    )

    # ---- Scheduling ----
    provider_cron_scheme: Mapped[Optional[str]] = mapped_column(
        String, nullable=True, comment="CronTab job schedule string"
    )
    collection_interval: Mapped[Optional[str]] = mapped_column(
        String, nullable=True, comment="Time range for video stream collection (e.g., 8:00-20:00)"
    )
    screenshot_interval: Mapped[Optional[int]] = mapped_column(
        Integer, nullable=True, comment="Interval between screenshots in minutes (e.g., 10)"
    )

    # ---- Analysis Configuration ----
    crop_zones: Mapped[Optional[dict]] = mapped_column(
        JSONB, nullable=True, comment="Screenshot crop zones configuration"
    )
    reference_image_url: Mapped[Optional[str]] = mapped_column(
        String, nullable=True, comment="Reference/standard image URL"
    )
    kpi_threshold: Mapped[Optional[float]] = mapped_column(
        Float, nullable=True, comment="KPI threshold (red line) - send notification below this percentage"
    )

    # ---- Notifications ----
    notification_chat_id: Mapped[Optional[str]] = mapped_column(
        String, nullable=True, comment="Chat ID for violation notifications"
    )

    # ---- Retry Logic ----
    retry_count: Mapped[int] = mapped_column(
        Integer, default=3, nullable=False, comment="Number of attempts to download image"
    )
    retry_timeout: Mapped[int] = mapped_column(
        Integer, default=5, nullable=False, comment="Timeout between retry attempts in seconds"
    )

    # ---- Status ----
    is_active: Mapped[bool] = mapped_column(
        Boolean, default=True, nullable=False
    )
