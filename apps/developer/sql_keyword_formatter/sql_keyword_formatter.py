#!/usr/bin/env python3
"""Uppercase common SQL keywords and place major clauses on new lines."""

from __future__ import annotations

import argparse
import re

DEFAULT_TEXT = "select name, score from players where score > 10 order by score desc"


def transform(text: str) -> str:
    """Transform or analyze input text."""
    keywords = (
        "select",
        "from",
        "where",
        "group by",
        "order by",
        "having",
        "limit",
        "join",
        "on",
        "as",
        "and",
        "or",
        "desc",
        "asc",
    )
    result = text
    for keyword in keywords:
        replacement = keyword.upper()
        if keyword in {
            "from",
            "where",
            "group by",
            "order by",
            "having",
            "limit",
            "join",
        }:
            replacement = f"\n{replacement}"
        result = re.sub(rf"\b{keyword}\b", replacement, result, flags=re.IGNORECASE)
    return result.strip()


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
