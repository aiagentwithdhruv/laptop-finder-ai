from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.laptop_repo import LaptopRepository
from app.schemas.compare import ComparisonResult, SpecComparison
from app.core.exceptions import BadRequestError


class ComparisonService:
    def __init__(self, db: AsyncSession):
        self.repo = LaptopRepository(db)

    async def compare(self, laptop_ids: list[UUID]) -> ComparisonResult:
        if len(laptop_ids) < 2 or len(laptop_ids) > 4:
            raise BadRequestError("Compare 2-4 laptops")

        laptops = await self.repo.get_multiple(laptop_ids)
        if len(laptops) != len(laptop_ids):
            raise BadRequestError("Some laptops not found")

        laptop_data = []
        for l in laptops:
            primary_img = next((i.url for i in l.images if i.is_primary), l.images[0].url if l.images else None)
            laptop_data.append({
                "id": str(l.id),
                "brand": l.brand,
                "model": l.model,
                "price": float(l.price),
                "avg_rating": float(l.avg_rating),
                "primary_image": primary_img,
            })

        specs = self._build_spec_comparisons(laptops)
        summary = self._build_summary(laptops)

        return ComparisonResult(laptops=laptop_data, specs=specs, summary=summary)

    def _build_spec_comparisons(self, laptops) -> list[SpecComparison]:
        fields = [
            ("price", "Price", lambda l: f"${float(l.price):,.2f}", "lower"),
            ("cpu", "Processor", lambda l: l.spec.cpu if l.spec else "N/A", None),
            ("ram_gb", "RAM", lambda l: f"{l.spec.ram_gb}GB {l.spec.ram_type}" if l.spec else "N/A", "higher_num"),
            ("storage_gb", "Storage", lambda l: f"{l.spec.storage_gb}GB {l.spec.storage_type}" if l.spec else "N/A", "higher_num"),
            ("gpu", "GPU", lambda l: l.spec.gpu if l.spec else "N/A", None),
            ("display", "Display", lambda l: f'{float(l.spec.display_size)}" {l.spec.display_type} {l.spec.display_refresh_rate}Hz' if l.spec else "N/A", None),
            ("battery", "Battery Life", lambda l: f"{float(l.spec.battery_life_hours)}h" if l.spec else "N/A", "higher_num"),
            ("weight", "Weight", lambda l: f"{float(l.spec.weight_kg)}kg" if l.spec else "N/A", "lower_num"),
            ("rating", "Rating", lambda l: f"{float(l.avg_rating)}/5 ({l.review_count} reviews)", "higher_num"),
        ]

        comparisons = []
        for field, label, extractor, winner_rule in fields:
            values = {f"{l.brand} {l.model}": extractor(l) for l in laptops}

            winner = None
            if winner_rule == "lower" and all(l.spec for l in laptops):
                winner_laptop = min(laptops, key=lambda l: float(l.price))
                winner = f"{winner_laptop.brand} {winner_laptop.model}"
            elif winner_rule == "higher_num" and field == "ram_gb":
                winner_laptop = max(laptops, key=lambda l: l.spec.ram_gb if l.spec else 0)
                winner = f"{winner_laptop.brand} {winner_laptop.model}"
            elif winner_rule == "higher_num" and field == "storage_gb":
                winner_laptop = max(laptops, key=lambda l: l.spec.storage_gb if l.spec else 0)
                winner = f"{winner_laptop.brand} {winner_laptop.model}"
            elif winner_rule == "higher_num" and field == "battery":
                winner_laptop = max(laptops, key=lambda l: float(l.spec.battery_life_hours) if l.spec else 0)
                winner = f"{winner_laptop.brand} {winner_laptop.model}"
            elif winner_rule == "lower_num" and field == "weight":
                winner_laptop = min(laptops, key=lambda l: float(l.spec.weight_kg) if l.spec else 999)
                winner = f"{winner_laptop.brand} {winner_laptop.model}"
            elif winner_rule == "higher_num" and field == "rating":
                winner_laptop = max(laptops, key=lambda l: float(l.avg_rating))
                winner = f"{winner_laptop.brand} {winner_laptop.model}"

            comparisons.append(SpecComparison(field=field, label=label, values=values, winner=winner))

        return comparisons

    def _build_summary(self, laptops) -> str:
        cheapest = min(laptops, key=lambda l: float(l.price))
        best_rated = max(laptops, key=lambda l: float(l.avg_rating))
        lightest = min(laptops, key=lambda l: float(l.spec.weight_kg) if l.spec else 999)

        parts = [
            f"Best value: {cheapest.brand} {cheapest.model} (${float(cheapest.price):,.2f}).",
            f"Highest rated: {best_rated.brand} {best_rated.model} ({float(best_rated.avg_rating)}/5).",
            f"Most portable: {lightest.brand} {lightest.model} ({float(lightest.spec.weight_kg) if lightest.spec else '?'}kg).",
        ]
        return " ".join(parts)
