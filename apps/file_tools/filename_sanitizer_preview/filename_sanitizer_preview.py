#!/usr/bin/env python3
"""Preview portable sanitized filenames without renaming anything."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


def inspect_path(path: Path) -> str:
    """Inspect path without modifying it."""
    entries = [path] if path.is_file() else sorted(path.iterdir())
    lines = []
    for item in entries:
        cleaned_stem = (
            re.sub(r"[^A-Za-z0-9._-]+", "_", item.stem).strip("._") or "unnamed"
        )
        cleaned = cleaned_stem + item.suffix.casefold()
        if item.name != cleaned:
            lines.append(f"{item.name} -> {cleaned}")
    return "\n".join(lines) or "No filename changes suggested."


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "path",
        nargs="?",
        type=Path,
        default=Path.cwd(),
        help="Path to inspect.",
    )
    return parser


def main() -> None:
    """Run command-line interface."""
    args = build_parser().parse_args()
    try:
        print(inspect_path(Path(args.path)))
    except (OSError, ValueError) as error:
        raise SystemExit(str(error)) from error


if __name__ == "__main__":
    main()
