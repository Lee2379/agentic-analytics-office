from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from agentic_analytics_office.orchestrator import run_workflow


ROOT = Path(__file__).resolve().parents[1]


class OrchestratorTests(unittest.TestCase):
    def test_all_role_stages_complete_and_emit_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            metrics = run_workflow(
                ROOT / "data" / "sample_products.csv",
                ROOT / "data" / "sample_sales.csv",
                output,
            )
            expected = {
                "executive_report.md",
                "forecast.svg",
                "metrics.json",
                "slack_payload.json",
                "trace.json",
            }
            self.assertEqual({path.name for path in output.iterdir()}, expected)
            self.assertTrue(metrics["qa"]["passed"])
            self.assertEqual(metrics["workflow"]["stages_completed"], 7)
            trace = json.loads((output / "trace.json").read_text(encoding="utf-8"))
            self.assertEqual([event["agent"] for event in trace], ["sam", "ada", "ethan", "mia", "noah", "sophie", "oliver"])
            self.assertTrue(all(event["status"] == "completed" for event in trace))


if __name__ == "__main__":
    unittest.main()
