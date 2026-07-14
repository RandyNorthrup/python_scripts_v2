#!/usr/bin/env python3
"""Score password variety and length without storing the input."""

from __future__ import annotations

import argparse

DEFAULT_TEXT = "Correct-Horse-9-Battery!"


def transform(text: str) -> str:
    """Transform or analyze input text."""
    checks = {
        "12+ characters": len(text) >= 12,
        "lowercase": any(character.islower() for character in text),
        "uppercase": any(character.isupper() for character in text),
        "digit": any(character.isdigit() for character in text),
        "symbol": any(not character.isalnum() for character in text),
    }
    score = sum(checks.values())
    details = "\n".join(
        f"[{'x' if passed else ' '}] {label}" for label, passed in checks.items()
    )
    return f"Score: {score}/{len(checks)}\n{details}"


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
