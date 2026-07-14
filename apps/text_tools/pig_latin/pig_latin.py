#!/usr/bin/env python3
"""Translate simple English words into playful Pig Latin."""

from __future__ import annotations

import argparse
import re

DEFAULT_TEXT = "python scripts are surprisingly handy"


def transform(text: str) -> str:
    """Transform or analyze input text."""

    def convert(word: str) -> str:
        match = re.match(r"([^aeiouAEIOU]*)(.*)", word)
        if match is None:
            return word
        prefix, rest = match.groups()
        return f"{rest}{prefix}ay" if prefix else f"{word}yay"

    return " ".join(convert(word) for word in text.split())


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
