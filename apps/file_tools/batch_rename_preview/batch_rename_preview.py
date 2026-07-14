#!/usr/bin/env python3
"""Preview sequential filenames for files in a directory."""

from __future__ import annotations

import argparse
from pathlib import Path


def inspect_path(path: Path) -> str:
    """Inspect path without modifying it."""
    if path.is_file():
        return f"001_{path.name}"
    files = sorted(
        (item for item in path.iterdir() if item.is_file()),
        key=lambda item: item.name.casefold(),
    )
    width = max(3, len(str(len(files))))
    return (
        "\n".join(
            f"{item.name} -> {index:0{width}d}_{item.name}"
            for index, item in enumerate(files, 1)
        )
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
