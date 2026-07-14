#!/usr/bin/env python3
"""Compare two numeric semantic versions separated by a vertical bar."""

from __future__ import annotations

import argparse

DEFAULT_TEXT = "2.4.1 | 2.5.0"


def transform(text: str) -> str:
    """Transform or analyze input text."""
    left, separator, right = text.partition("|")
    if not separator:
        return "Use VERSION_A | VERSION_B"

    def parse(value: str) -> tuple[int, int, int]:
        pieces = value.strip().lstrip("v").split(".")
        if len(pieces) != 3:
            error_message = "versions need three numeric parts"
            raise ValueError(error_message)
        return int(pieces[0]), int(pieces[1]), int(pieces[2])

    first, second = parse(left), parse(right)
    relation = (
        "equal to"
        if first == second
        else ("older than" if first < second else "newer than")
    )
    return f"{left.strip()} is {relation} {right.strip()}"


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
