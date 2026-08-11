from __future__ import annotations

import csv
import statistics
from collections import Counter
from datetime import date, timedelta
from pathlib import Path
from typing import Any

from .models import Product, SaleDay


PRODUCT_FIELDS = {
    "sku",
    "category",
    "brand",
    "price_krw",
    "list_price_krw",
    "rating",
    "review_count",
    "stock",
}
SALES_FIELDS = {"date", "units", "revenue_krw"}


def _require_fields(actual: set[str], required: set[str], source: Path) -> None:
    missing = sorted(required - actual)
    if missing:
        raise ValueError(f"{source}: missing required columns: {', '.join(missing)}")


def load_products(path: str | Path) -> list[Product]:
    source = Path(path)
    with source.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        _require_fields(set(reader.fieldnames or []), PRODUCT_FIELDS, source)
        products: list[Product] = []
        seen: set[str] = set()
        for line_number, row in enumerate(reader, start=2):
            try:
                product = Product(
                    sku=row["sku"].strip(),
                    category=row["category"].strip(),
                    brand=row["brand"].strip(),
                    price_krw=int(row["price_krw"]),
                    list_price_krw=int(row["list_price_krw"]),
                    rating=float(row["rating"]),
                    review_count=int(row["review_count"]),
                    stock=int(row["stock"]),
                )
            except (TypeError, ValueError) as exc:
                raise ValueError(f"{source}:{line_number}: invalid product value") from exc

            errors: list[str] = []
            if not product.sku:
                errors.append("empty sku")
            if product.sku in seen:
                errors.append(f"duplicate sku {product.sku}")
            if not product.category or not product.brand:
                errors.append("empty category or brand")
            if product.price_krw <= 0:
                errors.append("price must be positive")
            if product.list_price_krw < product.price_krw:
                errors.append("list price must be at least the selling price")
            if not 0.0 <= product.rating <= 5.0:
                errors.append("rating must be between 0 and 5")
            if product.review_count < 0 or product.stock < 0:
                errors.append("review_count and stock must be non-negative")
            if errors:
                raise ValueError(f"{source}:{line_number}: {'; '.join(errors)}")
            seen.add(product.sku)
            products.append(product)

    if not products:
        raise ValueError(f"{source}: no product records")
    return products


def load_sales(path: str | Path) -> list[SaleDay]:
    source = Path(path)
    with source.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        _require_fields(set(reader.fieldnames or []), SALES_FIELDS, source)
        sales: list[SaleDay] = []
        parsed_dates: list[date] = []
        seen: set[str] = set()
        for line_number, row in enumerate(reader, start=2):
            date_text = row["date"].strip()
            try:
                item = SaleDay(
                    date=date_text,
                    units=int(row["units"]),
                    revenue_krw=int(row["revenue_krw"]),
                )
            except (TypeError, ValueError) as exc:
                raise ValueError(f"{source}:{line_number}: invalid sales value") from exc
            errors: list[str] = []
            try:
                parsed_date = date.fromisoformat(item.date)
            except ValueError:
                parsed_date = None
                errors.append("date must use canonical ISO format YYYY-MM-DD")
            if parsed_date is not None and parsed_date.isoformat() != item.date:
                errors.append("date must use canonical ISO format YYYY-MM-DD")
            if item.date in seen:
                errors.append(f"duplicate date {item.date}")
            if item.units < 0 or item.revenue_krw < 0:
                errors.append("units and revenue must be non-negative")
            if errors:
                raise ValueError(f"{source}:{line_number}: {'; '.join(errors)}")
            assert parsed_date is not None
            seen.add(item.date)
            sales.append(item)
            parsed_dates.append(parsed_date)

    if len(sales) < 10:
        raise ValueError(f"{source}: at least 10 chronological observations are required")
    if parsed_dates != sorted(parsed_dates):
        raise ValueError(f"{source}: sales rows must be sorted chronologically")
    for previous, current in zip(parsed_dates, parsed_dates[1:]):
        if current != previous + timedelta(days=1):
            raise ValueError(
                f"{source}: sales rows must contain consecutive daily observations; "
                f"expected {(previous + timedelta(days=1)).isoformat()}, found {current.isoformat()}"
            )
    return sales


def market_summary(products: list[Product]) -> dict[str, Any]:
    prices = [product.price_krw for product in products]
    total_reviews = sum(product.review_count for product in products)
    weighted_rating = (
        sum(product.rating * product.review_count for product in products) / total_reviews
        if total_reviews
        else 0.0
    )
    category_counts = Counter(product.category for product in products)
    brand_counts = Counter(product.brand for product in products)
    discounted = [product for product in products if product.discount_rate > 0]
    top_reviewed = sorted(
        products,
        key=lambda product: (product.review_count, product.rating, product.sku),
        reverse=True,
    )[:3]
    return {
        "product_count": len(products),
        "average_price_krw": round(statistics.fmean(prices), 2),
        "median_price_krw": round(statistics.median(prices), 2),
        "min_price_krw": min(prices),
        "max_price_krw": max(prices),
        "discounted_share_pct": round(100 * len(discounted) / len(products), 2),
        "average_discount_pct": round(
            100 * statistics.fmean(product.discount_rate for product in products), 2
        ),
        "total_reviews": total_reviews,
        "review_weighted_rating": round(weighted_rating, 3),
        "total_stock": sum(product.stock for product in products),
        "category_counts": dict(sorted(category_counts.items())),
        "brand_counts": dict(sorted(brand_counts.items())),
        "top_reviewed_skus": [product.sku for product in top_reviewed],
    }
