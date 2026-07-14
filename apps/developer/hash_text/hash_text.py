#!/usr/bin/env python3
"""Calculate SHA-256 and SHA-512 digests for text."""

from __future__ import annotations

import argparse
import hashlib

DEFAULT_TEXT = "hash this reproducibly"


def transform(text: str) -> str:
    """Transform or analyze input text."""
    encoded = text.encode()
    return (
        f"SHA-256: {hashlib.sha256(encoded).hexdigest()}\n"
        f"SHA-512: {hashlib.sha512(encoded).hexdigest()}"
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
