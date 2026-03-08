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
        headers={"Cache-Control": "no-cache", "Connection": "keep-alive", "X-Accel-Buffering": "no"},
    )


@router.get("/debug")
async def debug_chat(db: AsyncSession = Depends(get_db)):
    """Quick diagnostic — tests each chat component."""
    results = {}
    from app.config import get_settings
    settings = get_settings()
    results["openai_key_set"] = bool(settings.openai_api_key)
    results["openai_key_prefix"] = settings.openai_api_key[:8] + "..." if settings.openai_api_key else "EMPTY"

    try:
        from app.rag.embeddings import get_embedding
        emb = await get_embedding("test")
        results["embedding"] = f"OK (dim={len(emb)})"
    except Exception as e:
        results["embedding"] = f"FAIL: {e}"

    try:
        from app.repositories.embedding_repo import EmbeddingRepository
        repo = EmbeddingRepository(db)
        emb = await get_embedding("gaming laptop")
        chunks = await repo.similarity_search(emb, top_k=2)
        results["retrieval"] = f"OK ({len(chunks)} chunks)"
    except Exception as e:
        results["retrieval"] = f"FAIL: {e}"

    return results


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
