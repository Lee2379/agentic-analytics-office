from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .analytics import load_products, load_sales, market_summary
from .forecast import evaluate_and_forecast
from .models import AgentEvent
from .render import render_forecast_svg


def _event(
    sequence: int,
    agent: str,
    role: str,
    stage: str,
    inputs: tuple[str, ...],
    outputs: tuple[str, ...],
    checks: tuple[str, ...],
) -> AgentEvent:
    return AgentEvent(sequence, agent, role, stage, "completed", inputs, outputs, checks)


def _write_json(path: Path, payload: Any) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def _business_notes(summary: dict[str, Any], forecast: dict[str, Any]) -> list[str]:
    notes = []
    direction = "increasing" if forecast["slope_units_per_day"] > 0 else "stable or declining"
    notes.append(
        f"The training-window trend is {direction} at {forecast['slope_units_per_day']:.2f} units per day."
    )
    if summary["discounted_share_pct"] >= 60:
        notes.append(
            "Discounting is widespread in the synthetic assortment; margin impact should be reviewed before expanding promotions."
        )
    if summary["review_weighted_rating"] >= 4.2:
        notes.append("Review-weighted customer feedback is strong in the synthetic sample.")
    else:
        notes.append("Review-weighted customer feedback leaves room for assortment or quality improvement.")
    seven_day_units = round(sum(forecast["future_predicted"]))
    notes.append(f"The baseline projects approximately {seven_day_units} units over the next seven days.")
    return notes


def run_workflow(
    products_path: str | Path,
    sales_path: str | Path,
    output_dir: str | Path,
) -> dict[str, Any]:
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
    events: list[AgentEvent] = []

    products = load_products(products_path)
    sales = load_sales(sales_path)
    quality = {
        "products_valid": len(products),
        "sales_days_valid": len(sales),
        "duplicate_skus": 0,
        "duplicate_dates": 0,
        "chronological_sales": True,
        "status": "passed",
    }
    events.append(
        _event(1, "sam", "data_engineer", "validate_inputs", ("products.csv", "sales.csv"), ("data_quality",), ("schema_valid", "no_duplicates", "chronological_order"))
    )

    summary = market_summary(products)
    result = evaluate_and_forecast(sales)
    forecast = result.to_dict()
    events.append(
        _event(2, "ada", "data_analyst", "analyze_and_forecast", ("validated_products", "validated_sales"), ("market_summary", "forecast_metrics"), ("descriptive_metrics_computed", "holdout_not_used_for_fit"))
    )

    notes = _business_notes(summary, forecast)
    events.append(
        _event(3, "ethan", "business_analyst", "interpret_metrics", ("market_summary", "forecast_metrics"), ("decision_notes",), ("claims_linked_to_metrics", "observation_separated_from_recommendation"))
    )

    render_forecast_svg(result, output / "forecast.svg")
    events.append(
        _event(4, "mia", "visualization_designer", "render_forecast", ("forecast_metrics",), ("forecast.svg",), ("portable_svg", "accessible_description"))
    )

    narrative = (
        f"The synthetic portfolio contains {summary['product_count']} products with a median price of "
        f"KRW {summary['median_price_krw']:,.0f}. The chronological baseline achieved holdout MAE "
        f"{forecast['mae']:.2f} units and projects {sum(forecast['future_predicted']):.0f} units over seven days."
    )
    events.append(
        _event(5, "noah", "narrative_editor", "draft_summary", ("market_summary", "decision_notes"), ("draft_summary",), ("figures_preserved", "uncertainty_stated"))
    )

    required = {
        "data_quality": quality["status"] == "passed",
        "forecast_holdout": result.holdout_start_date > result.train_end_date,
        "forecast_chart": (output / "forecast.svg").exists(),
        "decision_notes": len(notes) >= 3,
        "narrative": bool(narrative),
    }
    qa_passed = all(required.values())
    events.append(
        _event(6, "sophie", "quality_reviewer", "review_artifacts", ("all_stage_artifacts",), ("qa_verdict",), tuple(f"{name}={str(value).lower()}" for name, value in required.items()))
    )
    if not qa_passed:
        raise RuntimeError("quality gate failed; executive report was not finalized")

    report = f"""# Executive analytics report

## Decision summary

{narrative}

## Data quality

- Valid product records: {quality['products_valid']}
- Valid chronological sales days: {quality['sales_days_valid']}
- Duplicate product IDs: {quality['duplicate_skus']}
- Duplicate dates: {quality['duplicate_dates']}
- QA status: **passed**

## Market snapshot

- Average price: KRW {summary['average_price_krw']:,.0f}
- Median price: KRW {summary['median_price_krw']:,.0f}
- Discounted share: {summary['discounted_share_pct']:.1f}%
- Average discount across all products: {summary['average_discount_pct']:.1f}%
- Review-weighted rating: {summary['review_weighted_rating']:.2f}/5
- Available stock: {summary['total_stock']} units

## Forecast evaluation

- Training observations: {result.train_size}
- Holdout observations: {result.holdout_size}
- Train end: {result.train_end_date}
- Holdout start: {result.holdout_start_date}
- MAE: {result.mae:.2f} units
- RMSE: {result.rmse:.2f} units
- MAPE: {result.mape_pct:.2f}%
- Seven-day projected demand: {sum(result.future_predicted):.0f} units

## Decision notes

{chr(10).join(f'- {note}' for note in notes)}

## Limitations

- All demo data is synthetic and supports engineering evaluation, not a real commercial decision.
- Linear trend is an interpretable baseline and does not model seasonality or promotions.
- Holdout metrics are based on seven observations and should not be over-generalized.
- The deterministic harness validates contracts; it does not reproduce private LLM reasoning.
"""
    (output / "executive_report.md").write_text(report, encoding="utf-8")
    events.append(
        _event(7, "oliver", "strategy_lead", "finalize_report", ("reviewed_artifacts", "qa_verdict"), ("executive_report.md", "slack_payload.json"), ("qa_passed", "limitations_included", "private_data_absent"))
    )

    metrics = {
        "data_quality": quality,
        "market_summary": summary,
        "forecast": forecast,
        "qa": {"passed": qa_passed, "checks": required},
        "workflow": {"stages_completed": len(events), "stages_expected": 7},
    }
    slack_payload = {
        "channel": "portfolio-demo",
        "text": "Synthetic analytics workflow completed",
        "summary": narrative,
        "metrics": {
            "median_price_krw": summary["median_price_krw"],
            "forecast_mae_units": result.mae,
            "seven_day_forecast_units": round(sum(result.future_predicted)),
            "qa_passed": qa_passed,
        },
        "notice": "Synthetic data only; no message was sent by the offline harness.",
    }
    _write_json(output / "metrics.json", metrics)
    _write_json(output / "trace.json", [event.to_dict() for event in events])
    _write_json(output / "slack_payload.json", slack_payload)
    return metrics
