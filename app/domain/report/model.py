# app/domain/message/model.py
from sqlalchemy import String, Integer, ForeignKey, Text, Float
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional
from app.database.connection import Base
from app.common.audit_mixin import TimestampMixin


class Report(Base, TimestampMixin):
    __tablename__ = "report"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    camera_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("camera.id"), nullable=False, index=True
    )
    fill_percentage: Mapped[Optional[float]] = mapped_column(
        Float, nullable=True
    )
    compliance_percentage: Mapped[Optional[float]] = mapped_column(
        Float, nullable=True
    )
    screenshot_s3_url: Mapped[Optional[str]] = mapped_column(
        String, nullable=True
    )
    analysis_text: Mapped[Optional[str]] = mapped_column(
        Text, nullable=True
    )
