from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from agentic_analytics_office import __version__
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
                "run_manifest.json",
                "slack_payload.json",
                "trace.json",
            }
            self.assertEqual({path.name for path in output.iterdir()}, expected)
            self.assertTrue(metrics["qa"]["passed"])
            self.assertEqual(metrics["workflow"]["contract_version"], "1.1")
            self.assertEqual(metrics["workflow"]["stages_completed"], 7)
            trace = json.loads((output / "trace.json").read_text(encoding="utf-8"))
            self.assertEqual([event["agent"] for event in trace], ["sam", "ada", "ethan", "mia", "noah", "sophie", "oliver"])
            self.assertTrue(all(event["status"] == "completed" for event in trace))
            self.assertTrue(all(event["objective"] for event in trace))
            self.assertEqual(trace[-1]["reviewed_by"], "human")

            manifest = json.loads((output / "run_manifest.json").read_text(encoding="utf-8"))
            self.assertEqual(manifest["package_version"], __version__)
            self.assertTrue(manifest["synthetic_data"])
            self.assertIn("agent_contracts.json", manifest["inputs"])
            self.assertIn("bytes_canonical_json", manifest["inputs"]["agent_contracts.json"])
            self.assertEqual(set(manifest["artifacts"]), expected - {"run_manifest.json"})
            for name, record in manifest["artifacts"].items():
                payload = (output / name).read_text(encoding="utf-8").replace("\r\n", "\n").encode("utf-8")
                self.assertEqual(record["sha256"], hashlib.sha256(payload).hexdigest())
                self.assertEqual(record["bytes_utf8_lf"], len(payload))


if __name__ == "__main__":
    unittest.main()
