from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.services.comparison_service import ComparisonService
from app.schemas.compare import CompareRequest, ComparisonResult

router = APIRouter(prefix="/compare", tags=["compare"])


@router.post("", response_model=ComparisonResult)
async def compare_laptops(request: CompareRequest, db: AsyncSession = Depends(get_db)):
    service = ComparisonService(db)
    return await service.compare(request.laptop_ids)
