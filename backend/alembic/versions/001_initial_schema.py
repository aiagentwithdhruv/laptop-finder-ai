"""Initial schema with pgvector

Revision ID: 001
Revises:
Create Date: 2026-03-08
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID, JSON
from pgvector.sqlalchemy import Vector

revision = "001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute("CREATE EXTENSION IF NOT EXISTS vector")

    op.create_table(
        "laptops",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("brand", sa.String(100), nullable=False, index=True),
        sa.Column("model", sa.String(200), nullable=False),
        sa.Column("slug", sa.String(200), nullable=False, unique=True, index=True),
        sa.Column("category", sa.String(50), nullable=False, index=True),
        sa.Column("price", sa.Numeric(10, 2), nullable=False),
        sa.Column("original_price", sa.Numeric(10, 2), nullable=True),
        sa.Column("currency", sa.String(3), server_default="USD"),
        sa.Column("description", sa.Text, nullable=False),
        sa.Column("highlights", JSON, server_default="[]"),
        sa.Column("avg_rating", sa.Numeric(3, 2), server_default="0.00"),
        sa.Column("review_count", sa.Integer, server_default="0"),
        sa.Column("in_stock", sa.Boolean, server_default="true"),
        sa.Column("created_at", sa.DateTime, server_default=sa.text("now()")),
        sa.Column("updated_at", sa.DateTime, server_default=sa.text("now()")),
    )
    op.create_index("idx_laptops_price", "laptops", ["price"])

    op.create_table(
        "laptop_specs",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("laptop_id", UUID(as_uuid=True), sa.ForeignKey("laptops.id", ondelete="CASCADE"), unique=True),
        sa.Column("cpu", sa.String(200), nullable=False),
        sa.Column("cpu_brand", sa.String(50), nullable=False, index=True),
        sa.Column("gpu", sa.String(200), nullable=False),
        sa.Column("gpu_brand", sa.String(50), nullable=False, index=True),
        sa.Column("ram_gb", sa.Integer, nullable=False, index=True),
        sa.Column("ram_type", sa.String(50), nullable=False),
        sa.Column("storage_gb", sa.Integer, nullable=False, index=True),
        sa.Column("storage_type", sa.String(50), nullable=False),
        sa.Column("display_size", sa.Numeric(4, 1), nullable=False),
        sa.Column("display_resolution", sa.String(50), nullable=False),
        sa.Column("display_type", sa.String(100), nullable=False),
        sa.Column("display_refresh_rate", sa.Integer, nullable=False),
        sa.Column("battery_wh", sa.Numeric(5, 1), nullable=False),
        sa.Column("battery_life_hours", sa.Numeric(4, 1), nullable=False),
        sa.Column("weight_kg", sa.Numeric(4, 2), nullable=False),
        sa.Column("os", sa.String(100), nullable=False),
        sa.Column("ports", JSON, server_default="[]"),
        sa.Column("wifi", sa.String(50), nullable=False),
        sa.Column("bluetooth", sa.String(20), nullable=False),
        sa.Column("color", sa.String(50), nullable=False),
        sa.Column("year", sa.Integer, nullable=False),
    )

    op.create_table(
        "laptop_images",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("laptop_id", UUID(as_uuid=True), sa.ForeignKey("laptops.id", ondelete="CASCADE"), index=True),
        sa.Column("url", sa.Text, nullable=False),
        sa.Column("alt_text", sa.String(200), nullable=False),
        sa.Column("is_primary", sa.Boolean, server_default="false"),
        sa.Column("sort_order", sa.Integer, server_default="0"),
    )

    op.create_table(
        "reviews",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("laptop_id", UUID(as_uuid=True), sa.ForeignKey("laptops.id", ondelete="CASCADE"), index=True),
        sa.Column("reviewer_name", sa.String(100), nullable=False),
        sa.Column("rating", sa.Integer, nullable=False),
        sa.Column("title", sa.String(200), nullable=False),
        sa.Column("body", sa.Text, nullable=False),
        sa.Column("verified_purchase", sa.Boolean, server_default="true"),
        sa.Column("helpful_count", sa.Integer, server_default="0"),
        sa.Column("use_case", sa.String(50), nullable=False),
        sa.Column("created_at", sa.DateTime, server_default=sa.text("now()")),
    )

    op.create_table(
        "laptop_embeddings",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("laptop_id", UUID(as_uuid=True), sa.ForeignKey("laptops.id", ondelete="CASCADE"), index=True),
        sa.Column("chunk_type", sa.String(50), nullable=False),
        sa.Column("content", sa.Text, nullable=False),
        sa.Column("embedding", Vector(1536)),
        sa.Column("metadata", JSON, server_default="{}"),
        sa.Column("created_at", sa.DateTime, server_default=sa.text("now()")),
    )

    op.create_table(
        "chat_sessions",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("title", sa.String(200), server_default="'New Chat'"),
        sa.Column("created_at", sa.DateTime, server_default=sa.text("now()")),
        sa.Column("updated_at", sa.DateTime, server_default=sa.text("now()")),
    )

    op.create_table(
        "chat_messages",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("session_id", UUID(as_uuid=True), sa.ForeignKey("chat_sessions.id", ondelete="CASCADE"), index=True),
        sa.Column("role", sa.String(20), nullable=False),
        sa.Column("content", sa.Text, nullable=False),
        sa.Column("recommended_laptop_ids", JSON, nullable=True),
        sa.Column("sources", JSON, nullable=True),
        sa.Column("created_at", sa.DateTime, server_default=sa.text("now()")),
    )


def downgrade():
    op.drop_table("chat_messages")
    op.drop_table("chat_sessions")
    op.drop_table("laptop_embeddings")
    op.drop_table("reviews")
    op.drop_table("laptop_images")
    op.drop_table("laptop_specs")
    op.drop_table("laptops")
    op.execute("DROP EXTENSION IF EXISTS vector")
