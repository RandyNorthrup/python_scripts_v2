#!/usr/bin/env python3
"""Create deterministic fictional test data from a seed phrase."""

from __future__ import annotations

import argparse
import hashlib
import json

DEFAULT_TEXT = "demo-seed"


def transform(text: str) -> str:
    """Transform or analyze input text."""
    digest = hashlib.sha256(text.encode()).digest()
    first_names = ("Avery", "Jordan", "Morgan", "Riley", "Taylor")
    last_names = ("Quinn", "Rivera", "Patel", "Kim", "Okafor")
    first = first_names[digest[0] % len(first_names)]
    last = last_names[digest[1] % len(last_names)]
    number = int.from_bytes(digest[2:4]) % 10000
    return json.dumps(
        {
            "name": f"{first} {last}",
            "email": f"{first.casefold()}.{last.casefold()}{number}@example.test",
            "id": number,
        },
        indent=2,
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
