#!/usr/bin/env python3
"""Summarize CSV rows, columns, and missing cells."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


def inspect_path(path: Path) -> str:
    """Inspect path without modifying it."""
    target = path if path.is_file() else next(iter(sorted(path.rglob("*.csv"))), None)
    if target is None:
        return "No CSV file found. Pass a CSV path."
    with target.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.reader(handle))
    if not rows:
        return f"File: {target}\nEmpty CSV."
    width = max(len(row) for row in rows)
    missing = sum(
        width - len(row) + sum(not cell.strip() for cell in row) for row in rows
    )
    return (
        f"File: {target}\n"
        f"Data rows: {max(0, len(rows) - 1)}\n"
        f"Columns: {width}\n"
        f"Missing cells: {missing}"
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
