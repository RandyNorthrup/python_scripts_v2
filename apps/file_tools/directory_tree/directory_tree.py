#!/usr/bin/env python3
"""Print a compact, sorted directory tree."""

from __future__ import annotations

import argparse
from pathlib import Path


def inspect_path(path: Path) -> str:
    """Inspect path without modifying it."""
    if not path.is_dir():
        return path.name
    lines = [f"{path.resolve().name}/"]
    entries = sorted(path.rglob("*"), key=lambda item: item.as_posix().casefold())
    for item in entries[:200]:
        relative = item.relative_to(path)
        prefix = "  " * (len(relative.parts) - 1)
        lines.append(f"{prefix}{relative.name}{'/' if item.is_dir() else ''}")
    if len(entries) > 200:
        lines.append(f"… {len(entries) - 200} more entries")
    return "\n".join(lines)


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
