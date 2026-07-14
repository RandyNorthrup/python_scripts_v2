#!/usr/bin/env python3
"""Apply the reversible ROT13 substitution to text."""

from __future__ import annotations

import argparse
import codecs

DEFAULT_TEXT = "The treasure is under the bridge."


def transform(text: str) -> str:
    """Transform or analyze input text."""
    return codecs.encode(text, "rot_13")


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
