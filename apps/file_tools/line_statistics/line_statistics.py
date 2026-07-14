#!/usr/bin/env python3
"""Count text lines, blank lines, and longest line length."""

from __future__ import annotations

import argparse
from pathlib import Path


def inspect_path(path: Path) -> str:
    """Inspect path without modifying it."""
    target = (
        path
        if path.is_file()
        else next((item for item in path.rglob("*.py") if item.is_file()), None)
    )
    if target is None:
        return "No text candidate found."
    lines = target.read_text(encoding="utf-8", errors="replace").splitlines()
    blank = sum(not line.strip() for line in lines)
    longest = max((len(line) for line in lines), default=0)
    return (
        f"File: {target}\n"
        f"Lines: {len(lines)}\n"
        f"Blank: {blank}\n"
        f"Longest: {longest} characters"
    )


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
