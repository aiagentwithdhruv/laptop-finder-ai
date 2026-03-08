from uuid import UUID

from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.services.chat_service import ChatService
from app.schemas.chat import ChatRequest, ChatSessionResponse
from app.repositories.chat_repo import ChatRepository

router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("")
async def chat(request: ChatRequest, db: AsyncSession = Depends(get_db)):
    service = ChatService(db)

    return StreamingResponse(
        service.chat(
            message=request.message,
            session_id=request.session_id,
            conversation_history=request.conversation_history,
        ),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "Connection": "keep-alive"},
    )


@router.post("/sessions")
async def create_session(db: AsyncSession = Depends(get_db)):
    repo = ChatRepository(db)
    session = await repo.create_session()
    await db.commit()
    return {"session_id": str(session.id)}


@router.get("/sessions/{session_id}", response_model=ChatSessionResponse)
async def get_session(session_id: UUID, db: AsyncSession = Depends(get_db)):
    repo = ChatRepository(db)
    session = await repo.get_session(session_id)
    if not session:
        from app.core.exceptions import NotFoundError
        raise NotFoundError("Chat session not found")
    return session
