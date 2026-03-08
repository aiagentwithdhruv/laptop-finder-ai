from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.laptop import Laptop
from app.rag.embeddings import get_embeddings_batch
from app.repositories.embedding_repo import EmbeddingRepository


def laptop_to_spec_text(laptop: Laptop) -> str:
    spec = laptop.spec
    highlights = ", ".join(laptop.highlights) if laptop.highlights else ""
    ports = ", ".join(spec.ports) if spec.ports else ""

    return (
        f"{laptop.brand} {laptop.model}. Category: {laptop.category}. "
        f"Price: ${float(laptop.price):.2f}. "
        f"CPU: {spec.cpu} ({spec.cpu_brand}). GPU: {spec.gpu} ({spec.gpu_brand}). "
        f"RAM: {spec.ram_gb}GB {spec.ram_type}. "
        f"Storage: {spec.storage_gb}GB {spec.storage_type}. "
        f"Display: {float(spec.display_size)}\" {spec.display_type} {spec.display_resolution} "
        f"{spec.display_refresh_rate}Hz. "
        f"Battery: {float(spec.battery_life_hours)}h ({float(spec.battery_wh)}Wh). "
        f"Weight: {float(spec.weight_kg)}kg. OS: {spec.os}. "
        f"Ports: {ports}. WiFi: {spec.wifi}. Color: {spec.color}. "
        f"Year: {spec.year}. "
        f"Highlights: {highlights}. "
        f"Rating: {float(laptop.avg_rating)}/5 ({laptop.review_count} reviews). "
        f"{laptop.description}"
    )


def laptop_to_review_text(laptop: Laptop) -> str:
    if not laptop.reviews:
        return ""

    reviews_text = []
    for r in laptop.reviews[:5]:
        reviews_text.append(f"[{r.rating}/5 - {r.use_case}] {r.title}: {r.body}")

    use_cases = list(set(r.use_case for r in laptop.reviews))

    return (
        f"{laptop.brand} {laptop.model} reviews. "
        f"Average: {float(laptop.avg_rating)}/5 from {laptop.review_count} reviews. "
        f"Best for: {', '.join(use_cases)}. "
        f"Reviews: {' | '.join(reviews_text)}"
    )


def get_price_bucket(price: float) -> str:
    if price < 500:
        return "budget"
    elif price < 1000:
        return "mid"
    elif price < 2000:
        return "premium"
    return "flagship"


async def ingest_laptop(laptop: Laptop, db: AsyncSession) -> int:
    repo = EmbeddingRepository(db)
    texts = []
    chunk_types = []

    spec_text = laptop_to_spec_text(laptop)
    texts.append(spec_text)
    chunk_types.append("full_spec")

    review_text = laptop_to_review_text(laptop)
    if review_text:
        texts.append(review_text)
        chunk_types.append("reviews_summary")

    embeddings = await get_embeddings_batch(texts)

    metadata = {
        "laptop_id": str(laptop.id),
        "brand": laptop.brand,
        "category": laptop.category,
        "price": float(laptop.price),
        "price_bucket": get_price_bucket(float(laptop.price)),
        "ram_gb": laptop.spec.ram_gb if laptop.spec else 0,
        "cpu_brand": laptop.spec.cpu_brand if laptop.spec else "",
        "gpu_brand": laptop.spec.gpu_brand if laptop.spec else "",
    }

    for text, chunk_type, embedding in zip(texts, chunk_types, embeddings):
        await repo.upsert(
            laptop_id=laptop.id,
            chunk_type=chunk_type,
            content=text,
            embedding=embedding,
            metadata={**metadata, "chunk_type": chunk_type},
        )

    return len(texts)
