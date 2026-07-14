#!/usr/bin/env python3
"""Compare two short text blocks separated by a vertical bar."""

from __future__ import annotations

import argparse
import difflib

DEFAULT_TEXT = "alpha\nbeta | alpha\ngamma"


def transform(text: str) -> str:
    """Transform or analyze input text."""
    before, separator, after = text.partition("|")
    if not separator:
        return "Use BEFORE | AFTER"
    return (
        "".join(
            difflib.unified_diff(
                before.strip().splitlines(keepends=True),
                after.strip().splitlines(keepends=True),
                fromfile="before",
                tofile="after",
            )
        )
        or "No differences."
    )


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
