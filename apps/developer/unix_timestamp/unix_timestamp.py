#!/usr/bin/env python3
"""Convert an ISO-8601 datetime into a Unix timestamp."""

from __future__ import annotations

import argparse
from datetime import UTC, datetime

DEFAULT_TEXT = "2026-01-01T12:00:00+00:00"


def transform(text: str) -> str:
    """Transform or analyze input text."""
    moment = datetime.fromisoformat(text)
    if moment.tzinfo is None:
        moment = moment.replace(tzinfo=UTC)
    return (
        f"Unix seconds: {moment.timestamp():.0f}\n"
        f"UTC: {moment.astimezone(UTC).isoformat()}"
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
