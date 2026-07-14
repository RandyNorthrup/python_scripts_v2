#!/usr/bin/env python3
"""Compare two phrases separated by a vertical bar for anagram equality."""

from __future__ import annotations

import argparse

DEFAULT_TEXT = "Dormitory | Dirty room"


def transform(text: str) -> str:
    """Transform or analyze input text."""
    left, separator, right = text.partition("|")
    if not separator:
        return "Provide two phrases separated by |"

    def normalize(value: str) -> list[str]:
        return sorted(
            character.casefold() for character in value if character.isalnum()
        )

    return f"Anagram: {normalize(left) == normalize(right)}"


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
