#!/usr/bin/env python3
"""Calculate display pixel density from resolution and diagonal size."""

from __future__ import annotations

import argparse


def calculate(
    width_px: float, height_px: float, diagonal_inches: float
) -> dict[str, float]:
    """Calculate and return named results."""
    if width_px <= 0 or height_px <= 0 or diagonal_inches <= 0:
        error_message = "all inputs must be positive"
        raise ValueError(error_message)
    return {
        "Pixels per inch": float((width_px**2 + height_px**2) ** 0.5 / diagonal_inches),
    }


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--width-px", type=float, default=2560.0, help="Horizontal pixels."
    )
    parser.add_argument(
        "--height-px", type=float, default=1440.0, help="Vertical pixels."
    )
    parser.add_argument(
        "--diagonal-inches", type=float, default=27.0, help="Screen diagonal."
    )
    return parser


def main() -> None:
    """Run command-line interface."""
    args = build_parser().parse_args()
    try:
        results = calculate(
            width_px=float(args.width_px),
            height_px=float(args.height_px),
            diagonal_inches=float(args.diagonal_inches),
        )
    except ValueError as error:
        raise SystemExit(str(error)) from error
    for label, value in results.items():
        print(f"{label}: {value:,.2f}")


if __name__ == "__main__":
    main()
