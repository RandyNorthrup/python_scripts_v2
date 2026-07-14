#!/usr/bin/env python3
"""Encode text with a classic three-letter Caesar shift."""

from __future__ import annotations

import argparse

DEFAULT_TEXT = "Meet me by the old oak tree."


def transform(text: str) -> str:
    """Transform or analyze input text."""
    result: list[str] = []
    for character in text:
        if character.isascii() and character.isalpha():
            base = ord("A" if character.isupper() else "a")
            result.append(chr((ord(character) - base + 3) % 26 + base))
        else:
            result.append(character)
    return "".join(result)


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
