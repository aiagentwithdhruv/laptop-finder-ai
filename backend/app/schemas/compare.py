from pydantic import BaseModel
from uuid import UUID


class CompareRequest(BaseModel):
    laptop_ids: list[UUID]


class SpecComparison(BaseModel):
    field: str
    label: str
    values: dict[str, str]
    winner: str | None = None


class ComparisonResult(BaseModel):
    laptops: list[dict]
    specs: list[SpecComparison]
    summary: str
