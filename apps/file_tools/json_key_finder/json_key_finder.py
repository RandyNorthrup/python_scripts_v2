#!/usr/bin/env python3
"""List every dotted key path found in a JSON document."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def inspect_path(path: Path) -> str:
    """Inspect path without modifying it."""
    target = path if path.is_file() else next(iter(sorted(path.rglob("*.json"))), None)
    if target is None:
        return "No JSON file found. Pass a JSON path."
    data = json.loads(target.read_text(encoding="utf-8"))
    found: list[str] = []

    def walk(value: object, prefix: str = "") -> None:
        if isinstance(value, dict):
            for key, child in value.items():
                current = f"{prefix}.{key}" if prefix else str(key)
                found.append(current)
                walk(child, current)
        elif isinstance(value, list):
            for index, child in enumerate(value):
                walk(child, f"{prefix}[{index}]")

    walk(data)
    return "\n".join(found) or "No object keys found."


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
