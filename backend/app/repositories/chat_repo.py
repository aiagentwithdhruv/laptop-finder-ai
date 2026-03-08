from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.models.chat import ChatSession, ChatMessage


class ChatRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_session(self, title: str = "New Chat") -> ChatSession:
        session = ChatSession(title=title)
        self.db.add(session)
        await self.db.flush()
        return session

    async def get_session(self, session_id: UUID) -> ChatSession | None:
        result = await self.db.execute(
            select(ChatSession)
            .options(joinedload(ChatSession.messages))
            .where(ChatSession.id == session_id)
        )
        return result.unique().scalar_one_or_none()

    async def add_message(
        self,
        session_id: UUID,
        role: str,
        content: str,
        recommended_laptop_ids: list | None = None,
        sources: list | None = None,
    ) -> ChatMessage:
        message = ChatMessage(
            session_id=session_id,
            role=role,
            content=content,
            recommended_laptop_ids=recommended_laptop_ids,
            sources=sources,
        )
        self.db.add(message)
        await self.db.flush()
        return message
