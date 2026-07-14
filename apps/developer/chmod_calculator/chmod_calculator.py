#!/usr/bin/env python3
"""Convert a three-digit Unix permission mode into symbolic form."""

from __future__ import annotations

import argparse

DEFAULT_TEXT = "754"


def transform(text: str) -> str:
    """Transform or analyze input text."""
    if len(text) != 3 or any(character not in "01234567" for character in text):
        return "Provide a three-digit octal mode, such as 754."
    symbols = ""
    for digit in text:
        value = int(digit)
        symbols += "r" if value & 4 else "-"
        symbols += "w" if value & 2 else "-"
        symbols += "x" if value & 1 else "-"
    return f"{text}: {symbols}"


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
