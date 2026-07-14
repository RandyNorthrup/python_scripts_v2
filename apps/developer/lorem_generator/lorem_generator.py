#!/usr/bin/env python3
"""Generate a deterministic filler paragraph from a numeric word count."""

from __future__ import annotations

import argparse

DEFAULT_TEXT = "40"


def transform(text: str) -> str:
    """Transform or analyze input text."""
    words = [
        "lorem",
        "ipsum",
        "dolor",
        "sit",
        "amet",
        "consectetur",
        "adipiscing",
        "elit",
        "sed",
        "do",
        "eiusmod",
        "tempor",
        "incididunt",
        "ut",
        "labore",
        "et",
        "dolore",
        "magna",
        "aliqua",
    ]
    try:
        count = max(1, min(500, int(text)))
    except ValueError:
        return "Provide a word count from 1 to 500."
    return (
        " ".join(words[index % len(words)] for index in range(count)).capitalize() + "."
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
