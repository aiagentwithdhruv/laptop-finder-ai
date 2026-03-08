from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.services.seed_service import seed_database

router = APIRouter(prefix="/seed", tags=["seed"])


@router.post("")
async def seed(
    generate_embeddings: bool = Query(True, description="Also generate vector embeddings"),
    db: AsyncSession = Depends(get_db),
):
    result = await seed_database(db, generate_embeddings=generate_embeddings)
    return result
