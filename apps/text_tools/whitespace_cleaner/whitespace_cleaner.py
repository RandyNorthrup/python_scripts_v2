#!/usr/bin/env python3
"""Collapse repeated horizontal whitespace and trim every line."""

from __future__ import annotations

import argparse

DEFAULT_TEXT = "  Too   many   spaces.  \n  Another    line. "


def transform(text: str) -> str:
    """Transform or analyze input text."""
    return "\n".join(" ".join(line.split()) for line in text.splitlines())


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
