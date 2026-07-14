#!/usr/bin/env python3
"""Turn a title into a lowercase URL-friendly slug."""

from __future__ import annotations

import argparse
import re

DEFAULT_TEXT = "Ten Tiny Python Tools!"


def transform(text: str) -> str:
    """Transform or analyze input text."""
    lowered = text.casefold().strip()
    return re.sub(r"[^a-z0-9]+", "-", lowered).strip("-")


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
