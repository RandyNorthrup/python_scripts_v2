#!/usr/bin/env python3
"""Count common severity labels in a log file."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


def inspect_path(path: Path) -> str:
    """Inspect path without modifying it."""
    target = (
        path
        if path.is_file()
        else next((item for item in path.rglob("*.log") if item.is_file()), None)
    )
    if target is None:
        return "No log file found. Pass a log path."
    content = target.read_text(encoding="utf-8", errors="replace")
    levels = ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL")
    lines = []
    for level in levels:
        pattern = rf"\b{level}\b"
        count = len(re.findall(pattern, content, re.IGNORECASE))
        lines.append(f"{level}: {count}")
    return "\n".join(lines)


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
