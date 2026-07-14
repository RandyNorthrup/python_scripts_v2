#!/usr/bin/env python3
"""List sections and keys in an INI configuration file."""

from __future__ import annotations

import argparse
import configparser
from pathlib import Path


def inspect_path(path: Path) -> str:
    """Inspect path without modifying it."""
    target = path if path.is_file() else next(iter(sorted(path.rglob("*.ini"))), None)
    if target is None:
        return "No INI file found. Pass an INI path."
    parser = configparser.ConfigParser()
    parser.read(target, encoding="utf-8")
    lines = [
        f"[{section}]\n" + "\n".join(f"  {key}" for key in parser[section])
        for section in parser.sections()
    ]
    return "\n".join(lines) or "No sections found."


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
