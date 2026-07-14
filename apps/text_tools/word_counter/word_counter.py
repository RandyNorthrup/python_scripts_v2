#!/usr/bin/env python3
"""Count lines, words, and characters in text."""

from __future__ import annotations

import argparse

DEFAULT_TEXT = "Python makes small tools pleasant to build.\nThis is line two."


def transform(text: str) -> str:
    """Transform or analyze input text."""
    words = text.split()
    lines = text.splitlines() or [""]
    return f"Lines: {len(lines)}\nWords: {len(words)}\nCharacters: {len(text)}"


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
