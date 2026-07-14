#!/usr/bin/env python3
"""Show CSV headers and up to five example values per column."""

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
        reader = csv.DictReader(handle)
        rows = list(reader)[:5]
        headers = reader.fieldnames or []
    return (
        "\n".join(
            f"{header}: {', '.join(row.get(header, '') for row in rows)}"
            for header in headers
        )
        or "CSV has no headers."
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
