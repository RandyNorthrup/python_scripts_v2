"""Contract and smoke test for every standalone catalog app."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
APP_SCRIPTS = tuple(ROOT / item["script"] for item in MANIFEST)
MAX_SCRIPT_LINES = 3_000


@pytest.mark.parametrize("script", APP_SCRIPTS, ids=lambda path: path.parent.name)
def test_app_contract_and_smoke(script: Path, tmp_path: Path) -> None:
    """Give each app one test case covering files, help, and default demo."""
    directory = script.parent
    python_files = tuple(directory.glob("*.py"))
    assert python_files == (script,)
    assert (directory / "README.md").is_file()
    assert (directory / "requirements.txt").is_file()
    assert len(script.read_text(encoding="utf-8").splitlines()) < MAX_SCRIPT_LINES

    for extra_args in (("--help",), ()):
        result = subprocess.run(
            [sys.executable, str(script), *extra_args],
            cwd=tmp_path,
            check=False,
            capture_output=True,
            text=True,
            timeout=10,
        )
        assert result.returncode == 0, result.stderr
        assert result.stdout.strip()
