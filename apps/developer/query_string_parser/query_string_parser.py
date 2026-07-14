#!/usr/bin/env python3
"""Parse a URL query string into readable key-value pairs."""

from __future__ import annotations

import argparse
import urllib.parse

DEFAULT_TEXT = "page=2&tag=python&tag=tools&sort=new"


def transform(text: str) -> str:
    """Transform or analyze input text."""
    values = urllib.parse.parse_qs(text, keep_blank_values=True)
    return (
        "\n".join(f"{key}: {', '.join(items)}" for key, items in sorted(values.items()))
        or "No parameters."
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
