from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class PrivacyTests(unittest.TestCase):
    def test_repository_passes_privacy_scan(self) -> None:
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "privacy_scan.py"), str(ROOT)],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
