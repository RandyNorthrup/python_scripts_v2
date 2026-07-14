#!/usr/bin/env python3
"""List the largest files beneath a path."""

from __future__ import annotations

import argparse
from pathlib import Path


def inspect_path(path: Path) -> str:
    """Inspect path without modifying it."""
    files = (
        [path]
        if path.is_file()
        else [item for item in path.rglob("*") if item.is_file()]
    )
    largest = sorted(files, key=lambda item: item.stat().st_size, reverse=True)[:20]
    return (
        "\n".join(f"{item.stat().st_size:>12,}  {item}" for item in largest)
        or "No files found."
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
