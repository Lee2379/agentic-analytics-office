from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any


@dataclass(frozen=True)
class Product:
    sku: str
    category: str
    brand: str
    price_krw: int
    list_price_krw: int
    rating: float
    review_count: int
    stock: int

    @property
    def discount_rate(self) -> float:
        if self.list_price_krw <= 0:
            return 0.0
        return max(0.0, 1.0 - (self.price_krw / self.list_price_krw))


@dataclass(frozen=True)
class SaleDay:
    date: str
    units: int
    revenue_krw: int


@dataclass(frozen=True)
class ForecastResult:
    train_size: int
    holdout_size: int
    train_end_date: str
    holdout_start_date: str
    slope_units_per_day: float
    intercept: float
    mae: float
    rmse: float
    mape_pct: float | None
    mape_nonzero_observations: int
    holdout_actual: tuple[int, ...]
    holdout_predicted: tuple[float, ...]
    future_dates: tuple[str, ...]
    future_predicted: tuple[float, ...]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class AgentEvent:
    sequence: int
    agent: str
    role: str
    objective: str
    stage: str
    status: str
    input_artifacts: tuple[str, ...]
    output_artifacts: tuple[str, ...]
    checks: tuple[str, ...]
    reviewed_by: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
