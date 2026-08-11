from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from . import __version__
from .analytics import load_products, load_sales, market_summary
from .contracts import canonical_contract_bytes, load_agent_contracts
from .forecast import evaluate_and_forecast
from .models import AgentEvent
from .render import render_forecast_svg


def _event(
    sequence: int,
    contract: dict[str, Any],
    stage: str,
    checks: tuple[str, ...],
) -> AgentEvent:
    return AgentEvent(
        sequence=sequence,
        agent=contract["name"],
        role=contract["role"],
        objective=contract["objective"],
        stage=stage,
        status="completed",
        input_artifacts=tuple(contract["allowed_inputs"]),
        output_artifacts=tuple(contract["required_outputs"]),
        checks=checks,
        reviewed_by=contract["reviewed_by"],
    )


def _write_json(path: Path, payload: Any) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def _normalized_text_bytes(path: Path) -> bytes:
    """Return UTF-8/LF bytes so provenance is stable across Git checkout settings."""
    return path.read_text(encoding="utf-8").replace("\r\n", "\n").encode("utf-8")


def _file_record(path: Path) -> dict[str, Any]:
    payload = _normalized_text_bytes(path)
    return {
        "sha256": hashlib.sha256(payload).hexdigest(),
        "bytes_utf8_lf": len(payload),
    }


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
    contracts_path: str | Path | None = None,
) -> dict[str, Any]:
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
    events: list[AgentEvent] = []
    registry = load_agent_contracts(contracts_path)
    expected_agents = ("sam", "ada", "ethan", "mia", "noah", "sophie", "oliver")
    actual_agents = tuple(agent["name"] for agent in registry["agents"])
    if actual_agents != expected_agents:
        raise ValueError(
            "agent contracts must define the executable sequence: " + ", ".join(expected_agents)
        )
    contracts = {agent["name"]: agent for agent in registry["agents"]}

    products = load_products(products_path)
    sales = load_sales(sales_path)
    quality = {
        "products_valid": len(products),
        "sales_days_valid": len(sales),
        "duplicate_skus": 0,
        "duplicate_dates": 0,
        "chronological_sales": True,
        "consecutive_daily_sales": True,
        "status": "passed",
    }
    events.append(
        _event(
            1,
            contracts["sam"],
            "validate_inputs",
            ("schema_valid", "no_duplicates", "chronological_order", "daily_cadence"),
        )
    )

    summary = market_summary(products)
    result = evaluate_and_forecast(sales)
    forecast = result.to_dict()
    events.append(
        _event(
            2,
            contracts["ada"],
            "analyze_and_forecast",
            ("descriptive_metrics_computed", "holdout_not_used_for_fit"),
        )
    )

    notes = _business_notes(summary, forecast)
    events.append(
        _event(
            3,
            contracts["ethan"],
            "interpret_metrics",
            ("claims_linked_to_metrics", "observation_separated_from_recommendation"),
        )
    )

    render_forecast_svg(result, output / "forecast.svg")
    events.append(
        _event(
            4,
            contracts["mia"],
            "render_forecast",
            ("portable_svg", "accessible_description"),
        )
    )

    narrative = (
        f"The synthetic portfolio contains {summary['product_count']} products with a median price of "
        f"KRW {summary['median_price_krw']:,.0f}. The chronological baseline achieved holdout MAE "
        f"{forecast['mae']:.2f} units and projects {sum(forecast['future_predicted']):.0f} units over seven days."
    )
    events.append(
        _event(
            5,
            contracts["noah"],
            "draft_summary",
            ("figures_preserved", "uncertainty_stated"),
        )
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
        _event(
            6,
            contracts["sophie"],
            "review_artifacts",
            tuple(f"{name}={str(value).lower()}" for name, value in required.items()),
        )
    )
    if not qa_passed:
        raise RuntimeError("quality gate failed; executive report was not finalized")

    mape_display = (
        f"{result.mape_pct:.2f}%"
        if result.mape_pct is not None
        else "not defined (holdout contains no non-zero actuals)"
    )
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
- MAPE: {mape_display}
- MAPE observations: {result.mape_nonzero_observations}/{result.holdout_size} non-zero actuals
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
        _event(
            7,
            contracts["oliver"],
            "finalize_report",
            ("qa_passed", "limitations_included", "private_data_absent"),
        )
    )

    metrics = {
        "data_quality": quality,
        "market_summary": summary,
        "forecast": forecast,
        "qa": {"passed": qa_passed, "checks": required},
        "workflow": {
            "contract_version": registry["version"],
            "stages_completed": len(events),
            "stages_expected": 7,
        },
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

    artifact_names = (
        "executive_report.md",
        "forecast.svg",
        "metrics.json",
        "slack_payload.json",
        "trace.json",
    )
    contract_payload = canonical_contract_bytes(registry)
    input_records = {
        "products.csv": _file_record(Path(products_path)),
        "sales.csv": _file_record(Path(sales_path)),
        "agent_contracts.json": {
            "sha256": hashlib.sha256(contract_payload).hexdigest(),
            "bytes_canonical_json": len(contract_payload),
        },
    }
    run_basis = {
        "schema_version": "1.0",
        "package_version": __version__,
        "synthetic_data": True,
        "inputs": input_records,
    }
    run_id = hashlib.sha256(
        json.dumps(run_basis, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    manifest = {
        **run_basis,
        "run_id": run_id,
        "hash_normalization": {
            "text_files": "UTF-8 with LF line endings",
            "agent_contracts.json": "canonical JSON with sorted keys and no insignificant whitespace",
        },
        "artifacts": {name: _file_record(output / name) for name in artifact_names},
    }
    _write_json(output / "run_manifest.json", manifest)
    return metrics
