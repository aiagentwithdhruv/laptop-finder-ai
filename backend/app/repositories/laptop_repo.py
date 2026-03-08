from uuid import UUID

from sqlalchemy import select, func, desc, asc
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.models.laptop import Laptop, LaptopSpec
from app.schemas.laptop import LaptopFilter


class LaptopRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_id(self, laptop_id: UUID) -> Laptop | None:
        result = await self.db.execute(
            select(Laptop)
            .options(joinedload(Laptop.spec), joinedload(Laptop.images), joinedload(Laptop.reviews))
            .where(Laptop.id == laptop_id)
        )
        return result.unique().scalar_one_or_none()

    async def get_by_slug(self, slug: str) -> Laptop | None:
        result = await self.db.execute(
            select(Laptop)
            .options(joinedload(Laptop.spec), joinedload(Laptop.images), joinedload(Laptop.reviews))
            .where(Laptop.slug == slug)
        )
        return result.unique().scalar_one_or_none()

    async def list_laptops(self, filters: LaptopFilter) -> tuple[list[Laptop], int]:
        query = select(Laptop).options(joinedload(Laptop.spec), joinedload(Laptop.images))
        count_query = select(func.count(Laptop.id))

        if filters.brand:
            query = query.where(Laptop.brand == filters.brand)
            count_query = count_query.where(Laptop.brand == filters.brand)
        if filters.category:
            query = query.where(Laptop.category == filters.category)
            count_query = count_query.where(Laptop.category == filters.category)
        if filters.min_price is not None:
            query = query.where(Laptop.price >= filters.min_price)
            count_query = count_query.where(Laptop.price >= filters.min_price)
        if filters.max_price is not None:
            query = query.where(Laptop.price <= filters.max_price)
            count_query = count_query.where(Laptop.price <= filters.max_price)
        if filters.min_ram is not None:
            query = query.join(LaptopSpec).where(LaptopSpec.ram_gb >= filters.min_ram)
            count_query = count_query.join(LaptopSpec).where(LaptopSpec.ram_gb >= filters.min_ram)
        if filters.cpu_brand:
            if LaptopSpec not in [c.entity for c in query.column_descriptions]:
                query = query.join(LaptopSpec)
                count_query = count_query.join(LaptopSpec)
            query = query.where(LaptopSpec.cpu_brand == filters.cpu_brand)
            count_query = count_query.where(LaptopSpec.cpu_brand == filters.cpu_brand)
        if filters.gpu_brand:
            if LaptopSpec not in [c.entity for c in query.column_descriptions]:
                query = query.join(LaptopSpec)
                count_query = count_query.join(LaptopSpec)
            query = query.where(LaptopSpec.gpu_brand == filters.gpu_brand)
            count_query = count_query.where(LaptopSpec.gpu_brand == filters.gpu_brand)

        sort_map = {
            "price_asc": asc(Laptop.price),
            "price_desc": desc(Laptop.price),
            "rating": desc(Laptop.avg_rating),
            "newest": desc(Laptop.created_at),
        }
        query = query.order_by(sort_map.get(filters.sort_by, asc(Laptop.price)))

        total_result = await self.db.execute(count_query)
        total = total_result.scalar()

        offset = (filters.page - 1) * filters.page_size
        query = query.offset(offset).limit(filters.page_size)

        result = await self.db.execute(query)
        laptops = result.unique().scalars().all()

        return list(laptops), total

    async def search(self, query_text: str, page: int = 1, page_size: int = 12) -> tuple[list[Laptop], int]:
        pattern = f"%{query_text}%"
        query = (
            select(Laptop)
            .options(joinedload(Laptop.spec), joinedload(Laptop.images))
            .where(
                (Laptop.brand.ilike(pattern))
                | (Laptop.model.ilike(pattern))
                | (Laptop.description.ilike(pattern))
                | (Laptop.category.ilike(pattern))
            )
        )
        count_query = select(func.count(Laptop.id)).where(
            (Laptop.brand.ilike(pattern))
            | (Laptop.model.ilike(pattern))
            | (Laptop.description.ilike(pattern))
            | (Laptop.category.ilike(pattern))
        )

        total_result = await self.db.execute(count_query)
        total = total_result.scalar()

        offset = (page - 1) * page_size
        result = await self.db.execute(query.offset(offset).limit(page_size))
        laptops = result.unique().scalars().all()

        return list(laptops), total

    async def get_brands(self) -> list[str]:
        result = await self.db.execute(select(Laptop.brand).distinct().order_by(Laptop.brand))
        return [row[0] for row in result.all()]

    async def get_categories(self) -> list[str]:
        result = await self.db.execute(select(Laptop.category).distinct().order_by(Laptop.category))
        return [row[0] for row in result.all()]

    async def get_multiple(self, laptop_ids: list[UUID]) -> list[Laptop]:
        result = await self.db.execute(
            select(Laptop)
            .options(joinedload(Laptop.spec), joinedload(Laptop.images), joinedload(Laptop.reviews))
            .where(Laptop.id.in_(laptop_ids))
        )
        return list(result.unique().scalars().all())
