import json
from pathlib import Path

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.laptop import Laptop, LaptopSpec, LaptopImage
from app.models.review import Review
from app.rag.ingestion import ingest_laptop


async def seed_database(db: AsyncSession, generate_embeddings: bool = True) -> dict:
    # Clear existing data to avoid duplicates on re-seed
    from app.models.embedding import LaptopEmbedding
    await db.execute(LaptopEmbedding.__table__.delete())
    await db.execute(Review.__table__.delete())
    await db.execute(LaptopImage.__table__.delete())
    await db.execute(LaptopSpec.__table__.delete())
    await db.execute(Laptop.__table__.delete())
    await db.flush()

    data_path = Path(__file__).parent.parent.parent / "seed_data" / "laptops.json"
    with open(data_path) as f:
        laptops_data = json.load(f)

    laptops_created = 0
    reviews_created = 0
    embeddings_created = 0

    for item in laptops_data:
        laptop = Laptop(
            brand=item["brand"],
            model=item["model"],
            slug=item["slug"],
            category=item["category"],
            price=item["price"],
            original_price=item.get("original_price"),
            description=item["description"],
            highlights=item["highlights"],
            avg_rating=0.0,
            review_count=0,
        )
        db.add(laptop)
        await db.flush()

        spec_data = item["spec"]
        spec = LaptopSpec(laptop_id=laptop.id, **spec_data)
        db.add(spec)

        for img_data in item.get("images", []):
            image = LaptopImage(
                laptop_id=laptop.id,
                url=img_data["url"],
                alt_text=img_data["alt_text"],
                is_primary=img_data.get("is_primary", False),
                sort_order=img_data.get("sort_order", 0),
            )
            db.add(image)

        total_rating = 0
        for rev_data in item.get("reviews", []):
            review = Review(
                laptop_id=laptop.id,
                reviewer_name=rev_data["reviewer_name"],
                rating=rev_data["rating"],
                title=rev_data["title"],
                body=rev_data["body"],
                verified_purchase=rev_data.get("verified_purchase", True),
                helpful_count=rev_data.get("helpful_count", 0),
                use_case=rev_data.get("use_case", "general"),
            )
            db.add(review)
            total_rating += rev_data["rating"]
            reviews_created += 1

        review_count = len(item.get("reviews", []))
        if review_count > 0:
            laptop.avg_rating = round(total_rating / review_count, 2)
            laptop.review_count = review_count

        await db.flush()
        laptops_created += 1

        if generate_embeddings:
            await db.refresh(laptop, ["spec", "images", "reviews"])
            count = await ingest_laptop(laptop, db)
            embeddings_created += count

    await db.commit()

    return {
        "laptops_created": laptops_created,
        "reviews_created": reviews_created,
        "embeddings_created": embeddings_created,
    }
