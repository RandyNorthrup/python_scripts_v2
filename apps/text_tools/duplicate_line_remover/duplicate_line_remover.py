#!/usr/bin/env python3
"""Remove repeated lines while preserving first-seen order."""

from __future__ import annotations

import argparse

DEFAULT_TEXT = "apple\nbanana\napple\npear\nbanana"


def transform(text: str) -> str:
    """Transform or analyze input text."""
    seen: set[str] = set()
    unique: list[str] = []
    for line in text.splitlines():
        if line not in seen:
            seen.add(line)
            unique.append(line)
    return "\n".join(unique)


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "text",
        nargs="?",
        default=DEFAULT_TEXT,
        help="Text to process.",
    )
    return parser


def main() -> None:
    """Run command-line interface."""
    args = build_parser().parse_args()
    print(transform(str(args.text)))


if __name__ == "__main__":
    main()
