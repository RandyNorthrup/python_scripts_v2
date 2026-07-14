#!/usr/bin/env python3
"""Convert a six-digit hexadecimal color to RGB and HSL."""

from __future__ import annotations

import argparse
import colorsys
import re

DEFAULT_TEXT = "#4f86c6"


def transform(text: str) -> str:
    """Transform or analyze input text."""
    value = text.strip().lstrip("#")
    if not re.fullmatch(r"[0-9a-fA-F]{6}", value):
        return "Provide a six-digit hex color."
    red, green, blue = (int(value[index : index + 2], 16) for index in (0, 2, 4))
    hue, lightness, saturation = colorsys.rgb_to_hls(red / 255, green / 255, blue / 255)
    return (
        f"RGB: {red}, {green}, {blue}\n"
        f"HSL: {hue * 360:.0f}°, {saturation * 100:.0f}%, "
        f"{lightness * 100:.0f}%"
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
