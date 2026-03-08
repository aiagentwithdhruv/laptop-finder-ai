import uuid
from datetime import datetime

from sqlalchemy import String, Text, Numeric, Boolean, Integer, DateTime, ForeignKey, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID

from app.core.database import Base


class Laptop(Base):
    __tablename__ = "laptops"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    brand: Mapped[str] = mapped_column(String(100), index=True)
    model: Mapped[str] = mapped_column(String(200))
    slug: Mapped[str] = mapped_column(String(200), unique=True, index=True)
    category: Mapped[str] = mapped_column(String(50), index=True)
    price: Mapped[float] = mapped_column(Numeric(10, 2))
    original_price: Mapped[float | None] = mapped_column(Numeric(10, 2), nullable=True)
    currency: Mapped[str] = mapped_column(String(3), default="USD")
    description: Mapped[str] = mapped_column(Text)
    highlights: Mapped[list] = mapped_column(JSON, default=list)
    avg_rating: Mapped[float] = mapped_column(Numeric(3, 2), default=0.0)
    review_count: Mapped[int] = mapped_column(Integer, default=0)
    in_stock: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    spec: Mapped["LaptopSpec"] = relationship(back_populates="laptop", uselist=False, lazy="joined")
    images: Mapped[list["LaptopImage"]] = relationship(back_populates="laptop", lazy="joined", order_by="LaptopImage.sort_order")
    reviews: Mapped[list["Review"]] = relationship(back_populates="laptop", lazy="selectin")


class LaptopSpec(Base):
    __tablename__ = "laptop_specs"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    laptop_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("laptops.id", ondelete="CASCADE"), unique=True)
    cpu: Mapped[str] = mapped_column(String(200))
    cpu_brand: Mapped[str] = mapped_column(String(50), index=True)
    gpu: Mapped[str] = mapped_column(String(200))
    gpu_brand: Mapped[str] = mapped_column(String(50), index=True)
    ram_gb: Mapped[int] = mapped_column(Integer, index=True)
    ram_type: Mapped[str] = mapped_column(String(50))
    storage_gb: Mapped[int] = mapped_column(Integer, index=True)
    storage_type: Mapped[str] = mapped_column(String(50))
    display_size: Mapped[float] = mapped_column(Numeric(4, 1))
    display_resolution: Mapped[str] = mapped_column(String(50))
    display_type: Mapped[str] = mapped_column(String(100))
    display_refresh_rate: Mapped[int] = mapped_column(Integer)
    battery_wh: Mapped[float] = mapped_column(Numeric(5, 1))
    battery_life_hours: Mapped[float] = mapped_column(Numeric(4, 1))
    weight_kg: Mapped[float] = mapped_column(Numeric(4, 2))
    os: Mapped[str] = mapped_column(String(100))
    ports: Mapped[list] = mapped_column(JSON, default=list)
    wifi: Mapped[str] = mapped_column(String(50))
    bluetooth: Mapped[str] = mapped_column(String(20))
    color: Mapped[str] = mapped_column(String(50))
    year: Mapped[int] = mapped_column(Integer, default=2024)

    laptop: Mapped["Laptop"] = relationship(back_populates="spec")


class LaptopImage(Base):
    __tablename__ = "laptop_images"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    laptop_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("laptops.id", ondelete="CASCADE"), index=True)
    url: Mapped[str] = mapped_column(Text)
    alt_text: Mapped[str] = mapped_column(String(200))
    is_primary: Mapped[bool] = mapped_column(Boolean, default=False)
    sort_order: Mapped[int] = mapped_column(Integer, default=0)

    laptop: Mapped["Laptop"] = relationship(back_populates="images")
