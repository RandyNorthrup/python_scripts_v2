#!/usr/bin/env python3
"""Decode a JWT payload locally without claiming signature verification."""

from __future__ import annotations

import argparse
import base64
import json

DEFAULT_TEXT = "eyJhbGciOiJub25lIn0.eyJzdWIiOiJkZW1vIiwicm9sZSI6InJlYWRlciJ9."


def transform(text: str) -> str:
    """Transform or analyze input text."""
    parts = text.split(".")
    if len(parts) != 3:
        return "Expected three dot-separated JWT sections."
    payload = parts[1] + "=" * (-len(parts[1]) % 4)
    decoded = base64.urlsafe_b64decode(payload).decode()
    return json.dumps(json.loads(decoded), indent=2, sort_keys=True)


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
