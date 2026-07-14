#!/usr/bin/env python3
"""Explain the five fields of a basic cron expression."""

from __future__ import annotations

import argparse

DEFAULT_TEXT = "15 9 * * 1-5"


def transform(text: str) -> str:
    """Transform or analyze input text."""
    fields = text.split()
    if len(fields) != 5:
        return "Expected: minute hour day-of-month month day-of-week"
    labels = ("Minute", "Hour", "Day of month", "Month", "Day of week")
    return "\n".join(
        f"{label}: {value}" for label, value in zip(labels, fields, strict=True)
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
