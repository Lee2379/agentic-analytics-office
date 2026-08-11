from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from agentic_analytics_office.contracts import load_agent_contracts


ROOT = Path(__file__).resolve().parents[1]


class ContractTests(unittest.TestCase):
    def test_public_registry_matches_packaged_runtime_contracts(self) -> None:
        public_registry = json.loads(
            (ROOT / "config" / "agents.json").read_text(encoding="utf-8")
        )
        self.assertEqual(public_registry, load_agent_contracts())
        self.assertEqual(len(public_registry["agents"]), 7)

    def test_duplicate_agent_name_is_rejected(self) -> None:
        registry = load_agent_contracts()
        registry["agents"][1]["name"] = registry["agents"][0]["name"]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "agents.json"
            path.write_text(json.dumps(registry), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "duplicate agent name"):
                load_agent_contracts(path)


if __name__ == "__main__":
    unittest.main()
