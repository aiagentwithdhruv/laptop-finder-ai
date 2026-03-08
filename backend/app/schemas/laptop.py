from pydantic import BaseModel
from uuid import UUID


class LaptopSpecResponse(BaseModel):
    cpu: str
    cpu_brand: str
    gpu: str
    gpu_brand: str
    ram_gb: int
    ram_type: str
    storage_gb: int
    storage_type: str
    display_size: float
    display_resolution: str
    display_type: str
    display_refresh_rate: int
    battery_wh: float
    battery_life_hours: float
    weight_kg: float
    os: str
    ports: list[str]
    wifi: str
    bluetooth: str
    color: str
    year: int

    model_config = {"from_attributes": True}


class LaptopImageResponse(BaseModel):
    id: UUID
    url: str
    alt_text: str
    is_primary: bool

    model_config = {"from_attributes": True}


class ReviewResponse(BaseModel):
    id: UUID
    reviewer_name: str
    rating: int
    title: str
    body: str
    verified_purchase: bool
    helpful_count: int
    use_case: str

    model_config = {"from_attributes": True}


class LaptopResponse(BaseModel):
    id: UUID
    brand: str
    model: str
    slug: str
    category: str
    price: float
    original_price: float | None
    currency: str
    description: str
    highlights: list[str]
    avg_rating: float
    review_count: int
    in_stock: bool
    primary_image: str | None = None
    spec: LaptopSpecResponse | None = None

    model_config = {"from_attributes": True}


class LaptopDetailResponse(LaptopResponse):
    images: list[LaptopImageResponse] = []
    reviews: list[ReviewResponse] = []


class LaptopFilter(BaseModel):
    brand: str | None = None
    category: str | None = None
    min_price: float | None = None
    max_price: float | None = None
    min_ram: int | None = None
    cpu_brand: str | None = None
    gpu_brand: str | None = None
    sort_by: str = "price_asc"
    page: int = 1
    page_size: int = 12


class PaginatedResponse(BaseModel):
    items: list[LaptopResponse]
    total: int
    page: int
    page_size: int
    total_pages: int
