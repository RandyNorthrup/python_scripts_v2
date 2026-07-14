#!/usr/bin/env python3
"""Create initials from a person's or organization's name."""

from __future__ import annotations

import argparse

DEFAULT_TEXT = "National Aeronautics and Space Administration"


def transform(text: str) -> str:
    """Transform or analyze input text."""
    ignored = {"and", "of", "the"}
    return "".join(
        word[0].upper() for word in text.split() if word.casefold() not in ignored
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
