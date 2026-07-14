#!/usr/bin/env python3
"""Look up the standard phrase for an HTTP status code."""

from __future__ import annotations

import argparse
from http import HTTPStatus

DEFAULT_TEXT = "418"


def transform(text: str) -> str:
    """Transform or analyze input text."""
    try:
        status = HTTPStatus(int(text))
    except (ValueError, TypeError):
        return "Unknown or invalid HTTP status."
    return f"{status.value} {status.phrase}\n{status.description}"


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
