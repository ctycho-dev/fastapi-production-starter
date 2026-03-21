from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db.connection import Base
from app.common.audit_mixin import TimestampMixin
from app.enums.enums import RAGType


class Chat(Base, TimestampMixin):
    __tablename__ = "chats"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True
    )
    rag_type: Mapped[RAGType] = mapped_column(nullable=False, default=RAGType.CLASSIC)
    external_id: Mapped[str | None] = mapped_column(String(255), nullable=True, index=True)
