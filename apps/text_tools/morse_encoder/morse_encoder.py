#!/usr/bin/env python3
"""Encode letters and digits as International Morse code symbols."""

from __future__ import annotations

import argparse

DEFAULT_TEXT = "SOS Python 3"


def transform(text: str) -> str:
    """Transform or analyze input text."""
    symbols = [
        ".-",
        "-...",
        "-.-.",
        "-..",
        ".",
        "..-.",
        "--.",
        "....",
        "..",
        ".---",
        "-.-",
        ".-..",
        "--",
        "-.",
        "---",
        ".--.",
        "--.-",
        ".-.",
        "...",
        "-",
        "..-",
        "...-",
        ".--",
        "-..-",
        "-.--",
        "--..",
        "-----",
        ".----",
        "..---",
        "...--",
        "....-",
        ".....",
        "-....",
        "--...",
        "---..",
        "----.",
    ]
    codes = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", symbols, strict=True))
    return " / ".join(
        " ".join(codes.get(character, "?") for character in word.upper())
        for word in text.split()
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
