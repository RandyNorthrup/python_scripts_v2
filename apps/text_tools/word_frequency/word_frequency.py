#!/usr/bin/env python3
"""List words by descending frequency."""

from __future__ import annotations

import argparse
import re
from collections import Counter

DEFAULT_TEXT = "Red fish blue fish, one fish two fish."


def transform(text: str) -> str:
    """Transform or analyze input text."""
    words = re.findall(r"[\w']+", text.casefold())
    counts = Counter(words)
    return "\n".join(f"{word}: {count}" for word, count in counts.most_common())


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
