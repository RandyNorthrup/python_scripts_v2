#!/usr/bin/env python3
"""Compare KEY=VALUE blocks separated by a vertical bar without changing files."""

from __future__ import annotations

import argparse

DEFAULT_TEXT = "MODE=dev\nPORT=8000 | MODE=prod\nPORT=8000\nCACHE=on"


def transform(text: str) -> str:
    """Transform or analyze input text."""
    left, separator, right = text.partition("|")
    if not separator:
        return "Use ENV_A | ENV_B"

    def parse(block: str) -> dict[str, str]:
        return dict(
            line.split("=", 1) for line in block.strip().splitlines() if "=" in line
        )

    first, second = parse(left), parse(right)
    keys = sorted(first.keys() | second.keys())
    return (
        "\n".join(
            f"{key}: {first.get(key, '<missing>')} -> {second.get(key, '<missing>')}"
            for key in keys
            if first.get(key) != second.get(key)
        )
        or "No differences."
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
