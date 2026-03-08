import uuid
from datetime import datetime

from sqlalchemy import String, Text, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID

from app.core.database import Base


class Review(Base):
    __tablename__ = "reviews"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    laptop_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("laptops.id", ondelete="CASCADE"), index=True)
    reviewer_name: Mapped[str] = mapped_column(String(100))
    rating: Mapped[int] = mapped_column(Integer)
    title: Mapped[str] = mapped_column(String(200))
    body: Mapped[str] = mapped_column(Text)
    verified_purchase: Mapped[bool] = mapped_column(Boolean, default=True)
    helpful_count: Mapped[int] = mapped_column(Integer, default=0)
    use_case: Mapped[str] = mapped_column(String(50))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    laptop: Mapped["Laptop"] = relationship(back_populates="reviews")
