from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


def _normalized_bytes(path: Path) -> bytes:
    return path.read_text(encoding="utf-8").replace("\r\n", "\n").encode("utf-8")


def _files(directory: Path) -> dict[str, Path]:
    return {
        path.relative_to(directory).as_posix(): path
        for path in sorted(directory.rglob("*"))
        if path.is_file()
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Compare regenerated workflow outputs with the committed reference artifacts."
    )
    parser.add_argument("--reference", type=Path, default=Path("artifacts/sample_run"))
    parser.add_argument("--candidate", type=Path, default=Path("artifacts/ci_run"))
    args = parser.parse_args()

    reference = _files(args.reference)
    candidate = _files(args.candidate)
    if set(reference) != set(candidate):
        missing = sorted(set(reference) - set(candidate))
        unexpected = sorted(set(candidate) - set(reference))
        raise SystemExit(f"artifact set mismatch; missing={missing}, unexpected={unexpected}")

    mismatches: list[str] = []
    for name in reference:
        reference_hash = hashlib.sha256(_normalized_bytes(reference[name])).hexdigest()
        candidate_hash = hashlib.sha256(_normalized_bytes(candidate[name])).hexdigest()
        if reference_hash != candidate_hash:
            mismatches.append(name)
    if mismatches:
        raise SystemExit(f"reference artifact mismatch: {', '.join(mismatches)}")

    print(f"reference artifact verification passed: {len(reference)} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
