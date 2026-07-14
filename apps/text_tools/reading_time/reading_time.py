#!/usr/bin/env python3
"""Estimate reading and speaking time from word count."""

from __future__ import annotations

import argparse

DEFAULT_TEXT = "Clear writing helps readers move quickly through an idea."


def transform(text: str) -> str:
    """Transform or analyze input text."""
    word_count = len(text.split())
    return (
        f"Words: {word_count}\n"
        f"Reading minutes: {word_count / 200:.2f}\n"
        f"Speaking minutes: {word_count / 130:.2f}"
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
