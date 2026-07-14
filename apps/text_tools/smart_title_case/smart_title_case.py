#!/usr/bin/env python3
"""Capitalize a heading while keeping short connector words lowercase."""

from __future__ import annotations

import argparse

DEFAULT_TEXT = "a walk through the city of glass"


def transform(text: str) -> str:
    """Transform or analyze input text."""
    small_words = {
        "a",
        "an",
        "and",
        "as",
        "at",
        "by",
        "for",
        "in",
        "of",
        "on",
        "or",
        "the",
        "to",
    }
    words = text.casefold().split()
    titled = [
        word.capitalize()
        if index in {0, len(words) - 1} or word not in small_words
        else word
        for index, word in enumerate(words)
    ]
    return " ".join(titled)


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
