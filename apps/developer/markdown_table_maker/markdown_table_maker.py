#!/usr/bin/env python3
"""Convert semicolon-separated rows and comma-separated cells into a Markdown table."""

from __future__ import annotations

import argparse

DEFAULT_TEXT = "Name,Score;Ada,98;Grace,96"


def transform(text: str) -> str:
    """Transform or analyze input text."""
    rows = [[cell.strip() for cell in row.split(",")] for row in text.split(";")]
    if len(rows) < 2 or not rows[0]:
        return "Provide a header and at least one row."
    width = len(rows[0])
    if any(len(row) != width for row in rows):
        return "Every row must have the same cell count."
    header = "| " + " | ".join(rows[0]) + " |"
    divider = "| " + " | ".join("---" for _ in rows[0]) + " |"
    body_rows = ["| " + " | ".join(row) + " |" for row in rows[1:]]
    return "\n".join((header, divider, *body_rows))


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
