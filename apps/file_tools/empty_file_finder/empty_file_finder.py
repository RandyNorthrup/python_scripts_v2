#!/usr/bin/env python3
"""Find zero-byte files and empty directories without deleting them."""

from __future__ import annotations

import argparse
from pathlib import Path


def inspect_path(path: Path) -> str:
    """Inspect path without modifying it."""
    if path.is_file():
        return str(path) if path.stat().st_size == 0 else "File is not empty."
    empty_files = [
        item for item in path.rglob("*") if item.is_file() and item.stat().st_size == 0
    ]
    empty_dirs = [
        item for item in path.rglob("*") if item.is_dir() and not any(item.iterdir())
    ]
    lines = [
        *(f"FILE {item}" for item in empty_files),
        *(f"DIR  {item}" for item in empty_dirs),
    ]
    return "\n".join(lines) or "No empty files or directories found."


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
