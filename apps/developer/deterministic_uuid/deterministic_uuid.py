#!/usr/bin/env python3
"""Create a stable UUID from a text namespace value."""

from __future__ import annotations

import argparse
import uuid

DEFAULT_TEXT = "example-project/item-42"


def transform(text: str) -> str:
    """Transform or analyze input text."""
    return str(uuid.uuid5(uuid.NAMESPACE_URL, text))


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
