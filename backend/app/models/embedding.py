import uuid
from datetime import datetime

from sqlalchemy import String, Text, DateTime, ForeignKey, JSON
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
from pgvector.sqlalchemy import Vector

from app.core.database import Base


class LaptopEmbedding(Base):
    __tablename__ = "laptop_embeddings"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    laptop_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("laptops.id", ondelete="CASCADE"), index=True)
    chunk_type: Mapped[str] = mapped_column(String(50))
    content: Mapped[str] = mapped_column(Text)
    embedding = mapped_column(Vector(1536))
    metadata_: Mapped[dict] = mapped_column("metadata", JSON, default=dict)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
