from __future__ import annotations

import unittest
from datetime import date, timedelta
from pathlib import Path

from agentic_analytics_office.analytics import load_sales
from agentic_analytics_office.forecast import evaluate_and_forecast
from agentic_analytics_office.models import SaleDay


ROOT = Path(__file__).resolve().parents[1]


class ForecastTests(unittest.TestCase):
    def test_holdout_is_strictly_after_training_window(self) -> None:
        sales = load_sales(ROOT / "data" / "sample_sales.csv")
        result = evaluate_and_forecast(sales, holdout_size=7)
        self.assertLess(result.train_end_date, result.holdout_start_date)
        self.assertEqual(result.train_size, 28)
        self.assertEqual(result.holdout_size, 7)
        self.assertEqual(len(result.future_predicted), 7)
        self.assertGreaterEqual(result.mae, 0)
        self.assertGreaterEqual(result.rmse, result.mae)

    def test_forecast_is_deterministic(self) -> None:
        sales = load_sales(ROOT / "data" / "sample_sales.csv")
        self.assertEqual(evaluate_and_forecast(sales), evaluate_and_forecast(sales))

    def test_mape_is_undefined_when_holdout_actuals_are_all_zero(self) -> None:
        start = date(2026, 1, 1)
        sales = [
            SaleDay(
                date=(start + timedelta(days=index)).isoformat(),
                units=10 if index < 9 else 0,
                revenue_krw=0,
            )
            for index in range(12)
        ]
        result = evaluate_and_forecast(sales, holdout_size=3)
        self.assertIsNone(result.mape_pct)
        self.assertEqual(result.mape_nonzero_observations, 0)


if __name__ == "__main__":
    unittest.main()
