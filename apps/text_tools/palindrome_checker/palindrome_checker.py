#!/usr/bin/env python3
"""Check whether text reads the same after normalization."""

from __future__ import annotations

import argparse

DEFAULT_TEXT = "Never odd or even"


def transform(text: str) -> str:
    """Transform or analyze input text."""
    normalized = "".join(
        character.casefold() for character in text if character.isalnum()
    )
    return f"Normalized: {normalized}\nPalindrome: {normalized == normalized[::-1]}"


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
