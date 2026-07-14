#!/usr/bin/env python3
"""Count each vowel and draw a small text histogram."""

from __future__ import annotations

import argparse

DEFAULT_TEXT = "Education is an adventure."


def transform(text: str) -> str:
    """Transform or analyze input text."""
    lowered = text.casefold()
    return "\n".join(
        f"{vowel}: {'#' * lowered.count(vowel)} ({lowered.count(vowel)})"
        for vowel in "aeiou"
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
