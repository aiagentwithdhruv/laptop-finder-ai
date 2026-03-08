from uuid import UUID

from sqlalchemy import select, text, delete
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.embedding import LaptopEmbedding


class EmbeddingRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def upsert(self, laptop_id: UUID, chunk_type: str, content: str, embedding: list[float], metadata: dict):
        existing = await self.db.execute(
            select(LaptopEmbedding).where(
                LaptopEmbedding.laptop_id == laptop_id,
                LaptopEmbedding.chunk_type == chunk_type,
            )
        )
        record = existing.scalar_one_or_none()

        if record:
            record.content = content
            record.embedding = embedding
            record.metadata_ = metadata
        else:
            record = LaptopEmbedding(
                laptop_id=laptop_id,
                chunk_type=chunk_type,
                content=content,
                embedding=embedding,
                metadata_=metadata,
            )
            self.db.add(record)

        await self.db.flush()
        return record

    async def similarity_search(
        self, query_embedding: list[float], top_k: int = 8, price_max: float | None = None
    ) -> list[dict]:
        embedding_str = "[" + ",".join(str(x) for x in query_embedding) + "]"

        where_clause = ""
        if price_max:
            where_clause = f"AND (metadata->>'price')::float <= {price_max}"

        sql = text(f"""
            SELECT id, laptop_id, chunk_type, content, metadata,
                   1 - (embedding <=> CAST(:embedding AS vector)) AS similarity
            FROM laptop_embeddings
            WHERE 1=1 {where_clause}
            ORDER BY embedding <=> CAST(:embedding AS vector)
            LIMIT :top_k
        """)

        result = await self.db.execute(sql, {"embedding": embedding_str, "top_k": top_k})
        rows = result.fetchall()

        return [
            {
                "id": str(row[0]),
                "laptop_id": str(row[1]),
                "chunk_type": row[2],
                "content": row[3],
                "metadata": row[4],
                "similarity": float(row[5]),
            }
            for row in rows
        ]

    async def delete_by_laptop(self, laptop_id: UUID):
        await self.db.execute(delete(LaptopEmbedding).where(LaptopEmbedding.laptop_id == laptop_id))
