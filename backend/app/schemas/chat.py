from pydantic import BaseModel
from uuid import UUID


class ChatRequest(BaseModel):
    session_id: UUID | None = None
    message: str
    conversation_history: list[dict] = []


class ChatMessageResponse(BaseModel):
    id: UUID
    role: str
    content: str
    recommended_laptop_ids: list[UUID] | None = None
    sources: list[dict] | None = None

    model_config = {"from_attributes": True}


class ChatSessionResponse(BaseModel):
    id: UUID
    title: str
    messages: list[ChatMessageResponse] = []

    model_config = {"from_attributes": True}
