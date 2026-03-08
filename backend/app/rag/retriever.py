from sqlalchemy.ext.asyncio import AsyncSession

from app.config import get_settings
from app.rag.embeddings import get_embedding
from app.repositories.embedding_repo import EmbeddingRepository

settings = get_settings()


async def retrieve_relevant_laptops(
    query: str,
    db: AsyncSession,
    top_k: int | None = None,
    price_max: float | None = None,
) -> list[dict]:
    query_embedding = await get_embedding(query)

    repo = EmbeddingRepository(db)
    results = await repo.similarity_search(
        query_embedding=query_embedding,
        top_k=top_k or settings.retrieval_top_k,
        price_max=price_max,
    )

    seen_laptops = set()
    deduplicated = []
    for r in results:
        laptop_id = r["laptop_id"]
        if laptop_id not in seen_laptops and r["similarity"] >= settings.retrieval_score_threshold:
            seen_laptops.add(laptop_id)
            deduplicated.append(r)

    return deduplicated
