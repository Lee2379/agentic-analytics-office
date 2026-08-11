from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
HTML_LINK = re.compile(r"(?:href|src)=[\"']([^\"']+)[\"']", re.IGNORECASE)
IGNORED_DIRECTORIES = {".git", ".venv", "build", "dist"}


def _local_target(raw_target: str) -> str | None:
    target = raw_target.strip().strip("<>")
    if not target or target.startswith("#"):
        return None
    if " \"" in target:
        target = target.split(" \"", 1)[0]
    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc:
        return None
    return unquote(parsed.path)


def main() -> int:
    failures: list[str] = []
    checked = 0
    for document in sorted(ROOT.rglob("*.md")):
        if any(part in IGNORED_DIRECTORIES for part in document.relative_to(ROOT).parts):
            continue
        text = document.read_text(encoding="utf-8")
        targets = [match.group(1) for match in MARKDOWN_LINK.finditer(text)]
        targets.extend(match.group(1) for match in HTML_LINK.finditer(text))
        for raw_target in targets:
            local_target = _local_target(raw_target)
            if local_target is None:
                continue
            checked += 1
            resolved = (document.parent / local_target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                failures.append(
                    f"{document.relative_to(ROOT)}: link escapes repository: {raw_target}"
                )
                continue
            if not resolved.exists():
                failures.append(f"{document.relative_to(ROOT)}: missing target: {raw_target}")

    if failures:
        raise SystemExit("markdown link verification failed:\n" + "\n".join(failures))
    print(f"markdown link verification passed: {checked} local targets")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
