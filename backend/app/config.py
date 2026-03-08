from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    database_url: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/laptop_rec"
    openai_api_key: str = ""
    anthropic_api_key: str = ""

    embedding_model: str = "text-embedding-3-small"
    embedding_dimensions: int = 1536
    llm_model: str = "gpt-4o"
    retrieval_top_k: int = 8
    retrieval_score_threshold: float = 0.3

    cors_origins: list[str] = ["*"]

    model_config = {"env_file": ["../.env", ".env"], "extra": "ignore"}


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    assert settings.database_url, "DATABASE_URL is required"
    return settings
