#!/usr/bin/env python3
"""Summarize sentence count and average sentence length."""

from __future__ import annotations

import argparse
import re

DEFAULT_TEXT = (
    "Short tools teach ideas. They also solve real problems! Try changing this text?"
)


def transform(text: str) -> str:
    """Transform or analyze input text."""
    sentences = [part.strip() for part in re.split(r"[.!?]+", text) if part.strip()]
    words = text.split()
    average = len(words) / len(sentences) if sentences else 0.0
    return (
        f"Sentences: {len(sentences)}\n"
        f"Words: {len(words)}\n"
        f"Average words: {average:.2f}"
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
