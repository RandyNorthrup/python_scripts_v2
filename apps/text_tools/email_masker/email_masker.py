#!/usr/bin/env python3
"""Mask email usernames while preserving domains."""

from __future__ import annotations

import argparse
import re

DEFAULT_TEXT = "Contact alex.example@example.com or team@school.edu."


def transform(text: str) -> str:
    """Transform or analyze input text."""

    def mask(match: re.Match[str]) -> str:
        username, domain = match.group(1), match.group(2)
        visible = username[:1]
        return f"{visible}{'*' * max(3, len(username) - 1)}@{domain}"

    return re.sub(r"\b([A-Za-z0-9._%+-]+)@([A-Za-z0-9.-]+\.[A-Za-z]{2,})\b", mask, text)


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
