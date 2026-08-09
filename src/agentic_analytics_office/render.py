from __future__ import annotations

from datetime import date, timedelta
from html import escape
from pathlib import Path

from .models import ForecastResult


def render_forecast_svg(result: ForecastResult, path: str | Path) -> None:
    target = Path(path)
    width, height = 960, 440
    top, bottom = 100, 65
    panel_width = 370
    panel_height = height - top - bottom
    left_x, right_x = 70, 555
    values = list(result.holdout_actual) + list(result.holdout_predicted) + list(result.future_predicted)
    y_max = max(values) * 1.12 if values else 1
    y_min = max(0.0, min(values) * 0.88) if values else 0.0
    span = max(1.0, y_max - y_min)

    def point(panel_x: int, index: int, value: float, count: int) -> tuple[float, float]:
        x = panel_x + index * panel_width / max(1, count - 1)
        y = top + (y_max - value) * panel_height / span
        return x, y

    holdout_count = len(result.holdout_actual)
    actual_points = [
        point(left_x, index, value, holdout_count)
        for index, value in enumerate(result.holdout_actual)
    ]
    predicted_points = [
        point(left_x, index, value, holdout_count)
        for index, value in enumerate(result.holdout_predicted)
    ]
    future_points = [
        point(right_x, index, value, len(result.future_predicted))
        for index, value in enumerate(result.future_predicted)
    ]

    def polyline(points: list[tuple[float, float]]) -> str:
        return " ".join(f"{x:.1f},{y:.1f}" for x, y in points)

    grid: list[str] = []
    labels: list[str] = []
    for step in range(5):
        value = y_min + span * step / 4
        y = top + (y_max - value) * panel_height / span
        grid.append(
            f'<line x1="{left_x}" y1="{y:.1f}" x2="{left_x+panel_width}" y2="{y:.1f}" class="grid"/>'
        )
        grid.append(
            f'<line x1="{right_x}" y1="{y:.1f}" x2="{right_x+panel_width}" y2="{y:.1f}" class="grid"/>'
        )
        labels.append(
            f'<text x="{left_x-12}" y="{y+4:.1f}" text-anchor="end" class="axis">{value:.0f}</text>'
        )

    holdout_start = date.fromisoformat(result.holdout_start_date)
    holdout_dates = [
        (holdout_start + timedelta(days=offset)).isoformat()
        for offset in range(holdout_count)
    ]
    holdout_label_dates = {
        holdout_dates[0],
        holdout_dates[len(holdout_dates) // 2],
        holdout_dates[-1],
    }
    holdout_labels = "".join(
        f'<text x="{x:.1f}" y="{height-bottom+22}" text-anchor="middle" class="axis">{escape(day[5:])}</text>'
        for (x, _), day in zip(actual_points, holdout_dates)
        if day in holdout_label_dates
    )
    future_label_dates = {
        result.future_dates[0],
        result.future_dates[len(result.future_dates) // 2],
        result.future_dates[-1],
    }
    future_labels = "".join(
        f'<text x="{x:.1f}" y="{height-bottom+22}" text-anchor="middle" class="axis">{escape(day[5:])}</text>'
        for (x, _), day in zip(future_points, result.future_dates)
        if day in future_label_dates
    )
    content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">Chronological holdout evaluation and seven-day demand forecast</title>
<desc id="desc">The left panel compares actual holdout demand with baseline predictions. The right panel shows future predicted daily units.</desc>
<style>
  .bg {{ fill:#081c24; }} .grid {{ stroke:#21434d; stroke-width:1; }}
  .axis {{ fill:#b9c9ce; font:12px system-ui,sans-serif; }}
  .heading {{ fill:#f5f8f9; font:600 20px system-ui,sans-serif; }}
  .sub {{ fill:#9fb4bb; font:13px system-ui,sans-serif; }}
  .actual {{ fill:none; stroke:#28c2a0; stroke-width:4; }}
  .pred {{ fill:none; stroke:#f58b45; stroke-width:3; stroke-dasharray:8 6; }}
  .future {{ fill:none; stroke:#5aa9ff; stroke-width:4; }}
  .legend {{ fill:#dbe6e9; font:13px system-ui,sans-serif; }}
</style>
<rect class="bg" width="100%" height="100%" rx="16"/>
<text x="{left_x}" y="30" class="heading">Demand forecast evaluation</text>
<text x="{left_x}" y="52" class="sub">Chronological split · no holdout leakage · units/day</text>
{''.join(grid)}{''.join(labels)}
<text x="{left_x}" y="82" class="legend">Holdout: actual vs baseline prediction</text>
<text x="{right_x}" y="82" class="legend">Future: seven-day baseline</text>
<g><polyline points="{polyline(actual_points)}" class="actual"/><polyline points="{polyline(predicted_points)}" class="pred"/>{holdout_labels}</g>
<g><polyline points="{polyline(future_points)}" class="future"/>{future_labels}</g>
<g transform="translate(68,{height-22})"><line x1="0" y1="0" x2="24" y2="0" class="actual"/><text x="32" y="4" class="legend">actual</text>
<line x1="105" y1="0" x2="129" y2="0" class="pred"/><text x="137" y="4" class="legend">holdout prediction</text>
<line x1="310" y1="0" x2="334" y2="0" class="future"/><text x="342" y="4" class="legend">future forecast</text></g>
</svg>'''
    target.write_text(content, encoding="utf-8")
