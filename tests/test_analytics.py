from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from agentic_analytics_office.analytics import load_products, load_sales, market_summary


ROOT = Path(__file__).resolve().parents[1]


class AnalyticsTests(unittest.TestCase):
    def test_product_summary_is_computed_from_validated_rows(self) -> None:
        products = load_products(ROOT / "data" / "sample_products.csv")
        summary = market_summary(products)
        self.assertEqual(summary["product_count"], 15)
        self.assertGreater(summary["average_price_krw"], 0)
        self.assertGreaterEqual(summary["review_weighted_rating"], 0)
        self.assertLessEqual(summary["review_weighted_rating"], 5)
        self.assertEqual(sum(summary["category_counts"].values()), 15)

    def test_duplicate_sku_is_rejected(self) -> None:
        content = (
            "sku,category,brand,price_krw,list_price_krw,rating,review_count,stock\n"
            "SYN-X,shirts,Demo,1000,1200,4.0,1,2\n"
            "SYN-X,shirts,Demo,1000,1200,4.0,1,2\n"
        )
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "products.csv"
            path.write_text(content, encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "duplicate sku"):
                load_products(path)

    def test_sales_are_chronological(self) -> None:
        sales = load_sales(ROOT / "data" / "sample_sales.csv")
        self.assertEqual(len(sales), 35)
        self.assertEqual([item.date for item in sales], sorted(item.date for item in sales))


if __name__ == "__main__":
    unittest.main()
