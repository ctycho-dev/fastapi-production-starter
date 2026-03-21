from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.enums.enums import RAGType
from app.common.base_repository import BaseRepository
from app.domain.chat.model import Chat


class ChatRepo(BaseRepository[Chat]):
    def __init__(self) -> None:
        super().__init__(Chat)

    async def list_for_user(
        self,
        session: AsyncSession,
        user_id: int,
        limit: int = 50,
        offset: int = 0,
    ) -> list[Chat]:
        result = await session.execute(
            select(Chat)
            .where(Chat.user_id == user_id)
            .order_by(Chat.created_at.desc())
            .limit(limit)
            .offset(offset)
        )
        return list(result.scalars().all())
    
    async def find_by_user_and_rag_type(
        self,
        session: AsyncSession,
        user_id: int,
        rag_type: RAGType,
    ) -> Chat | None:
        result = await session.execute(
            select(Chat)
            .where(Chat.user_id == user_id, Chat.rag_type == rag_type)
            .order_by(Chat.created_at.desc())
            .limit(1)
        )
        return result.scalars().first()

    async def find_by_external(
        self,
        session: AsyncSession,
        user_id: int,
        rag_type: RAGType,
        external_id: str,
    ) -> Chat | None:
        result = await session.execute(
            select(Chat).where(
                Chat.user_id == user_id,
                Chat.rag_type == rag_type,
                Chat.external_id == external_id,
            )
        )
        return result.scalars().first()
