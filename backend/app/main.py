from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import get_settings
from app.api.routes import laptops, chat, compare, seed

settings = get_settings()

app = FastAPI(title="Laptop Recommendation System", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(laptops.router, prefix="/api/v1")
app.include_router(chat.router, prefix="/api/v1")
app.include_router(compare.router, prefix="/api/v1")
app.include_router(seed.router, prefix="/api/v1")


@app.get("/health")
async def health():
    return {"status": "ok"}
