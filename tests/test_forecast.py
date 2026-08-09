from __future__ import annotations

import unittest
from pathlib import Path

from agentic_analytics_office.analytics import load_sales
from agentic_analytics_office.forecast import evaluate_and_forecast


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


if __name__ == "__main__":
    unittest.main()
