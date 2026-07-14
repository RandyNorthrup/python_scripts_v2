#!/usr/bin/env python3
"""Test a regular expression against text separated by a vertical bar."""

from __future__ import annotations

import argparse
import re

DEFAULT_TEXT = "\\bP\\w+ | Python powers practical projects"


def transform(text: str) -> str:
    """Transform or analyze input text."""
    pattern, separator, sample = text.partition("|")
    if not separator:
        return "Use PATTERN | TEXT"
    matches = re.findall(pattern.strip(), sample.strip())
    return f"Matches: {len(matches)}\n{matches!r}"


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
