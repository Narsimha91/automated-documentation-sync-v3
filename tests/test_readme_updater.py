from pathlib import Path

import pytest

from scripts.update_readme import END_MARKER, START_MARKER, update_readme


def test_update_readme_preserves_content_outside_markers(tmp_path: Path) -> None:
    readme_path = tmp_path / "README.md"
    original = (
        f"before\r\n{START_MARKER}\r\nold content\r\n{END_MARKER}\r\nafter\r\n"
    ).encode("utf-8")
    readme_path.write_bytes(original)

    assert update_readme(readme_path, ["add", "divide by zero"])

    expected = (
        f"before\r\n{START_MARKER}\n- add\n- divide by zero\n"
        f"{END_MARKER}\r\nafter\r\n"
    ).encode("utf-8")
    assert readme_path.read_bytes() == expected


def test_invalid_markers_fail_without_modifying_readme(tmp_path: Path) -> None:
    readme_path = tmp_path / "README.md"
    original = f"before\n{START_MARKER}\nmissing end".encode("utf-8")
    readme_path.write_bytes(original)

    with pytest.raises(ValueError):
        update_readme(readme_path, ["add"])

    assert readme_path.read_bytes() == original