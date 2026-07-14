#!/usr/bin/env python3
"""Encode UTF-8 text as Base64."""

from __future__ import annotations

import argparse
import base64

DEFAULT_TEXT = "Python bytes are explicit."


def transform(text: str) -> str:
    """Transform or analyze input text."""
    return base64.b64encode(text.encode()).decode()


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
