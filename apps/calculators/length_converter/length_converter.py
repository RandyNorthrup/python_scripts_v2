#!/usr/bin/env python3
"""Convert meters into common metric and imperial lengths."""

from __future__ import annotations

import argparse


def calculate(meters: float) -> dict[str, float]:
    """Calculate and return named results."""
    return {
        "Centimeters": float(meters * 100),
        "Feet": float(meters * 3.28084),
        "Inches": float(meters * 39.3701),
    }


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--meters", type=float, default=5.0, help="Length in meters.")
    return parser


def main() -> None:
    """Run command-line interface."""
    args = build_parser().parse_args()
    try:
        results = calculate(
            meters=float(args.meters),
        )
    except ValueError as error:
        raise SystemExit(str(error)) from error
    for label, value in results.items():
        print(f"{label}: {value:,.2f}")


if __name__ == "__main__":
    main()
