from __future__ import annotations

import math
from datetime import date, timedelta

from .models import ForecastResult, SaleDay


def _fit_linear(values: list[int]) -> tuple[float, float]:
    n = len(values)
    x_mean = (n - 1) / 2
    y_mean = sum(values) / n
    denominator = sum((x - x_mean) ** 2 for x in range(n))
    slope = (
        sum((x - x_mean) * (y - y_mean) for x, y in enumerate(values)) / denominator
        if denominator
        else 0.0
    )
    intercept = y_mean - slope * x_mean
    return slope, intercept


def _predict(slope: float, intercept: float, indexes: list[int]) -> list[float]:
    return [max(0.0, intercept + slope * index) for index in indexes]


def evaluate_and_forecast(sales: list[SaleDay], holdout_size: int = 7) -> ForecastResult:
    if holdout_size < 1 or holdout_size >= len(sales) - 2:
        raise ValueError("holdout_size must leave at least three training observations")

    train = sales[:-holdout_size]
    holdout = sales[-holdout_size:]
    train_values = [item.units for item in train]
    slope, intercept = _fit_linear(train_values)
    holdout_indexes = list(range(len(train), len(sales)))
    holdout_predicted = _predict(slope, intercept, holdout_indexes)
    holdout_actual = [item.units for item in holdout]
    errors = [actual - predicted for actual, predicted in zip(holdout_actual, holdout_predicted)]
    mae = sum(abs(error) for error in errors) / len(errors)
    rmse = math.sqrt(sum(error**2 for error in errors) / len(errors))
    nonzero = [
        abs((actual - predicted) / actual)
        for actual, predicted in zip(holdout_actual, holdout_predicted)
        if actual != 0
    ]
    mape = 100 * sum(nonzero) / len(nonzero) if nonzero else None

    full_slope, full_intercept = _fit_linear([item.units for item in sales])
    future_indexes = list(range(len(sales), len(sales) + 7))
    future_predicted = _predict(full_slope, full_intercept, future_indexes)
    last_date = date.fromisoformat(sales[-1].date)
    future_dates = [(last_date + timedelta(days=offset)).isoformat() for offset in range(1, 8)]

    return ForecastResult(
        train_size=len(train),
        holdout_size=len(holdout),
        train_end_date=train[-1].date,
        holdout_start_date=holdout[0].date,
        slope_units_per_day=round(slope, 4),
        intercept=round(intercept, 4),
        mae=round(mae, 4),
        rmse=round(rmse, 4),
        mape_pct=round(mape, 4) if mape is not None else None,
        mape_nonzero_observations=len(nonzero),
        holdout_actual=tuple(holdout_actual),
        holdout_predicted=tuple(round(value, 3) for value in holdout_predicted),
        future_dates=tuple(future_dates),
        future_predicted=tuple(round(value, 3) for value in future_predicted),
    )
