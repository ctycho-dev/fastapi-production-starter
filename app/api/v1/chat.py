from fastapi import APIRouter, Depends, Request, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.chat.schema import (
    ChatCreateSchema,
    ChatUpdateSchema,
    ChatOutSchema,
)
from app.domain.chat.service import ChatService
from app.domain.user.schema import UserOutSchema
from app.api.dependencies.db import get_session
from app.api.dependencies.services import get_chat_service
from app.api.dependencies.auth import get_current_user
from app.core.config import settings
from app.middleware.rate_limiter import limiter
from app.core.logger import get_logger

logger = get_logger(__name__)

router = APIRouter(prefix=settings.api.v1.chat, tags=["Chat"])


@router.post("", status_code=status.HTTP_201_CREATED, response_model=ChatOutSchema)
@limiter.limit("30/minute")
async def create_chat(
    request: Request,
    payload: ChatCreateSchema,
    session: AsyncSession = Depends(get_session),
    current_user: UserOutSchema = Depends(get_current_user),
    service: ChatService = Depends(get_chat_service),
):
    return await service.create(session, payload, current_user=current_user)


@router.get("", response_model=list[ChatOutSchema])
@limiter.limit("60/minute")
async def list_chats(
    request: Request,
    limit: int = 50,
    offset: int = 0,
    session: AsyncSession = Depends(get_session),
    current_user: UserOutSchema = Depends(get_current_user),
    service: ChatService = Depends(get_chat_service),
):
    return await service.list_for_user(
        session,
        user_id=current_user.id,
        limit=limit,
        offset=offset,
    )


@router.get("/{chat_id}", response_model=ChatOutSchema)
@limiter.limit("60/minute")
async def get_chat(
    request: Request,
    chat_id: int,
    session: AsyncSession = Depends(get_session),
    current_user: UserOutSchema = Depends(get_current_user),
    service: ChatService = Depends(get_chat_service),
):
    return await service.get_by_id(session, chat_id=chat_id, current_user=current_user)


@router.patch("/{chat_id}", response_model=ChatOutSchema)
@limiter.limit("30/minute")
async def update_chat(
    request: Request,
    chat_id: int,
    payload: ChatUpdateSchema,
    session: AsyncSession = Depends(get_session),
    current_user: UserOutSchema = Depends(get_current_user),
    service: ChatService = Depends(get_chat_service),
):
    return await service.update(
        session,
        chat_id=chat_id,
        data=payload,
        current_user=current_user,
    )


@router.delete("/{chat_id}", status_code=status.HTTP_204_NO_CONTENT)
@limiter.limit("30/minute")
async def delete_chat(
    request: Request,
    chat_id: int,
    session: AsyncSession = Depends(get_session),
    current_user: UserOutSchema = Depends(get_current_user),
    service: ChatService = Depends(get_chat_service),
):
    await service.delete_by_id(session, chat_id=chat_id, current_user=current_user)
