from __future__ import annotations

import os
import sys
import tempfile
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.features import features

START_MARKER = "<!-- docs-sync:start -->"
END_MARKER = "<!-- docs-sync:end -->"


def render_readme(content: str, feature_labels: list[str]) -> str:
    if content.count(START_MARKER) != 1 or content.count(END_MARKER) != 1:
        raise ValueError("README must contain exactly one start and end sync marker")

    start = content.index(START_MARKER) + len(START_MARKER)
    end = content.index(END_MARKER)
    if start > end:
        raise ValueError("README sync markers are out of order")

    if not isinstance(feature_labels, list):
        raise TypeError("features() must return a list of strings")
    if any(
        not isinstance(label, str)
        or not label.strip()
        or "\n" in label
        or "\r" in label
        for label in feature_labels
    ):
        raise ValueError("feature labels must be non-empty single-line strings")

    rendered_labels = "\n".join(f"- {label}" for label in feature_labels)
    return f"{content[:start]}\n{rendered_labels}\n{content[end:]}"


def update_readme(readme_path: Path, feature_labels: list[str]) -> bool:
    original = readme_path.read_bytes().decode("utf-8")
    updated = render_readme(original, feature_labels)
    if updated == original:
        return False

    temporary_path: str | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="wb", dir=readme_path.parent, delete=False
        ) as temporary_file:
            temporary_file.write(updated.encode("utf-8"))
            temporary_path = temporary_file.name
        os.replace(temporary_path, readme_path)
    finally:
        if temporary_path is not None and os.path.exists(temporary_path):
            os.unlink(temporary_path)
    return True


def main() -> int:
    try:
        changed = update_readme(PROJECT_ROOT / "README.md", features())
    except Exception as error:
        print(f"README update failed: {error}", file=sys.stderr)
        return 1

    print("README updated." if changed else "README already up to date.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())