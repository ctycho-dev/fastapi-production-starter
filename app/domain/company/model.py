from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional
from app.database.connection import Base
from app.common.audit_mixin import UserAuditMixin, TimestampMixin


class Company(Base, TimestampMixin, UserAuditMixin):
    __tablename__ = "company"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )

    name: Mapped[str] = mapped_column(String, nullable=False)
    
    address: Mapped[Optional[str]] = mapped_column(String, nullable=True)
