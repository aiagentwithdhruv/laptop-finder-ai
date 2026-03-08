from uuid import UUID

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.services.laptop_service import LaptopService
from app.schemas.laptop import LaptopFilter, LaptopDetailResponse, PaginatedResponse

router = APIRouter(prefix="/laptops", tags=["laptops"])


@router.get("", response_model=PaginatedResponse)
async def list_laptops(
    brand: str | None = None,
    category: str | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
    min_ram: int | None = None,
    cpu_brand: str | None = None,
    gpu_brand: str | None = None,
    sort_by: str = "price_asc",
    page: int = Query(1, ge=1),
    page_size: int = Query(12, ge=1, le=50),
    db: AsyncSession = Depends(get_db),
):
    service = LaptopService(db)
    filters = LaptopFilter(
        brand=brand, category=category,
        min_price=min_price, max_price=max_price,
        min_ram=min_ram, cpu_brand=cpu_brand, gpu_brand=gpu_brand,
        sort_by=sort_by, page=page, page_size=page_size,
    )
    return await service.list_laptops(filters)


@router.get("/search", response_model=PaginatedResponse)
async def search_laptops(
    q: str = Query(..., min_length=1),
    page: int = Query(1, ge=1),
    page_size: int = Query(12, ge=1, le=50),
    db: AsyncSession = Depends(get_db),
):
    service = LaptopService(db)
    return await service.search_laptops(q, page, page_size)


@router.get("/brands")
async def get_brands(db: AsyncSession = Depends(get_db)):
    service = LaptopService(db)
    return await service.get_brands()


@router.get("/categories")
async def get_categories(db: AsyncSession = Depends(get_db)):
    service = LaptopService(db)
    return await service.get_categories()


@router.get("/{laptop_id}", response_model=LaptopDetailResponse)
async def get_laptop(laptop_id: UUID, db: AsyncSession = Depends(get_db)):
    service = LaptopService(db)
    return await service.get_laptop(laptop_id)
