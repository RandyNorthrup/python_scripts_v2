#!/usr/bin/env python3
"""Find exact duplicate files using size and SHA-256 without deleting anything."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


def inspect_path(path: Path) -> str:
    """Inspect path without modifying it."""
    files = (
        [path]
        if path.is_file()
        else [item for item in path.rglob("*") if item.is_file()]
    )
    by_size: dict[int, list[Path]] = {}
    for item in files:
        by_size.setdefault(item.stat().st_size, []).append(item)
    by_digest: dict[str, list[Path]] = {}
    for same_size in by_size.values():
        if len(same_size) > 1:
            for item in same_size:
                digest = hashlib.sha256(item.read_bytes()).hexdigest()
                by_digest.setdefault(digest, []).append(item)
    groups = [items for items in by_digest.values() if len(items) > 1]
    return (
        "\n\n".join(
            "Duplicate group:\n" + "\n".join(str(item) for item in items)
            for items in groups
        )
        or "No exact duplicates found."
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
