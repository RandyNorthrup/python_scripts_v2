#!/usr/bin/env python3
"""Percent-encode text for safe URL query use."""

from __future__ import annotations

import argparse
import urllib.parse

DEFAULT_TEXT = "tea & biscuits / 2"


def transform(text: str) -> str:
    """Transform or analyze input text."""
    return urllib.parse.quote(text, safe="")


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
