from sqlalchemy import String, Text, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.database.connection import Base
from app.common.audit_mixin import TimestampMixin
from app.domain.report.model import Report


class Notification(Base, TimestampMixin):
    __tablename__ = "notification"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    text: Mapped[str] = mapped_column(Text, nullable=False)
    status: Mapped[str] = mapped_column(String, nullable=False)
    report_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("report.id"), nullable=True, index=True
    )
