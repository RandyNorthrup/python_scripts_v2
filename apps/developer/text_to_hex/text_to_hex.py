#!/usr/bin/env python3
"""Show UTF-8 bytes as hexadecimal and decimal values."""

from __future__ import annotations

import argparse

DEFAULT_TEXT = "Python 🐍"


def transform(text: str) -> str:
    """Transform or analyze input text."""
    encoded = text.encode()
    return (
        f"Hex: {encoded.hex(' ')}\nBytes: {' '.join(str(value) for value in encoded)}"
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
