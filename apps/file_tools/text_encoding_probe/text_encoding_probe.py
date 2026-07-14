#!/usr/bin/env python3
"""Check whether a file decodes as UTF-8, UTF-8 with BOM, or Latin-1."""

from __future__ import annotations

import argparse
from pathlib import Path


def inspect_path(path: Path) -> str:
    """Inspect path without modifying it."""
    target = (
        path
        if path.is_file()
        else next((item for item in path.rglob("*") if item.is_file()), None)
    )
    if target is None:
        return "No file found."
    data = target.read_bytes()
    for encoding in ("utf-8-sig", "utf-8", "latin-1"):
        try:
            decoded = data.decode(encoding)
        except UnicodeDecodeError:
            continue
        replacement_count = decoded.count("�")
        return (
            f"File: {target}\n"
            f"Compatible encoding: {encoding}\n"
            f"Characters: {len(decoded)}\n"
            f"Replacement characters: {replacement_count}"
        )
    return "No tested encoding succeeded."


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
