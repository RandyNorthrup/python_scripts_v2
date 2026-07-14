#!/usr/bin/env python3
"""Find TODO, FIXME, and NOTE markers in text files."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


def inspect_path(path: Path) -> str:
    """Inspect path without modifying it."""
    files = (
        [path]
        if path.is_file()
        else [
            item
            for item in path.rglob("*")
            if item.is_file()
            and item.suffix.casefold() in {".py", ".md", ".txt", ".js", ".ts"}
        ]
    )
    matches: list[str] = []
    pattern = re.compile(r"\b(TODO|FIXME|NOTE)\b", re.IGNORECASE)
    for item in files:
        for number, line in enumerate(
            item.read_text(encoding="utf-8", errors="replace").splitlines(), 1
        ):
            if pattern.search(line):
                matches.append(f"{item}:{number}: {line.strip()}")
    return "\n".join(matches[:200]) or "No markers found."


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
