#!/usr/bin/env python3
"""Extract labels and targets from inline Markdown links."""

from __future__ import annotations

import argparse
import re

DEFAULT_TEXT = (
    "Read [Python](https://python.org) and [PEP 8](https://peps.python.org/pep-0008/)."
)


def transform(text: str) -> str:
    """Transform or analyze input text."""
    links = re.findall(r"\[([^]]+)]\(([^)]+)\)", text)
    return (
        "\n".join(f"{label}: {target}" for label, target in links) or "No links found."
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
