from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.laptop_repo import LaptopRepository
from app.schemas.laptop import LaptopFilter, LaptopResponse, LaptopDetailResponse, PaginatedResponse
from app.core.exceptions import NotFoundError
import math


class LaptopService:
    def __init__(self, db: AsyncSession):
        self.repo = LaptopRepository(db)

    async def get_laptop(self, laptop_id: UUID) -> LaptopDetailResponse:
        laptop = await self.repo.get_by_id(laptop_id)
        if not laptop:
            raise NotFoundError(f"Laptop {laptop_id} not found")

        return self._to_detail_response(laptop)

    async def list_laptops(self, filters: LaptopFilter) -> PaginatedResponse:
        laptops, total = await self.repo.list_laptops(filters)
        total_pages = math.ceil(total / filters.page_size) if total > 0 else 0

        return PaginatedResponse(
            items=[self._to_response(l) for l in laptops],
            total=total,
            page=filters.page,
            page_size=filters.page_size,
            total_pages=total_pages,
        )

    async def search_laptops(self, query: str, page: int = 1, page_size: int = 12) -> PaginatedResponse:
        laptops, total = await self.repo.search(query, page, page_size)
        total_pages = math.ceil(total / page_size) if total > 0 else 0

        return PaginatedResponse(
            items=[self._to_response(l) for l in laptops],
            total=total,
            page=page,
            page_size=page_size,
            total_pages=total_pages,
        )

    async def get_brands(self) -> list[str]:
        return await self.repo.get_brands()

    async def get_categories(self) -> list[str]:
        return await self.repo.get_categories()

    def _to_response(self, laptop) -> LaptopResponse:
        primary_image = None
        if laptop.images:
            primary = next((i for i in laptop.images if i.is_primary), None)
            primary_image = (primary or laptop.images[0]).url if laptop.images else None

        return LaptopResponse(
            id=laptop.id,
            brand=laptop.brand,
            model=laptop.model,
            slug=laptop.slug,
            category=laptop.category,
            price=float(laptop.price),
            original_price=float(laptop.original_price) if laptop.original_price else None,
            currency=laptop.currency,
            description=laptop.description,
            highlights=laptop.highlights or [],
            avg_rating=float(laptop.avg_rating),
            review_count=laptop.review_count,
            in_stock=laptop.in_stock,
            primary_image=primary_image,
            spec=laptop.spec,
        )

    def _to_detail_response(self, laptop) -> LaptopDetailResponse:
        base = self._to_response(laptop)
        return LaptopDetailResponse(
            **base.model_dump(),
            images=laptop.images or [],
            reviews=laptop.reviews or [],
        )
