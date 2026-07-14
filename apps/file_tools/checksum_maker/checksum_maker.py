#!/usr/bin/env python3
"""Calculate SHA-256 checksums for a file or directory."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


def inspect_path(path: Path) -> str:
    """Inspect path without modifying it."""
    files = (
        [path]
        if path.is_file()
        else sorted(item for item in path.rglob("*") if item.is_file())[:100]
    )
    lines = []
    for item in files:
        digest = hashlib.sha256(item.read_bytes()).hexdigest()
        lines.append(f"{digest}  {item}")
    return "\n".join(lines) or "No files found."


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
