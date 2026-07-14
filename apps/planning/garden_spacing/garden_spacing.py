#!/usr/bin/env python3
"""Estimate plant capacity for a rectangular garden bed."""

from __future__ import annotations

import argparse


def calculate(length_m: float, width_m: float, spacing_cm: float) -> dict[str, float]:
    """Calculate and return named results."""
    if length_m <= 0 or width_m <= 0 or spacing_cm <= 0:
        error_message = "dimensions must be positive"
        raise ValueError(error_message)
    return {
        "Area square meters": float(length_m * width_m),
        "Approximate plants": float(length_m * width_m / (spacing_cm / 100) ** 2),
    }


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--length-m", type=float, default=3.0, help="Bed length.")
    parser.add_argument("--width-m", type=float, default=1.2, help="Bed width.")
    parser.add_argument("--spacing-cm", type=float, default=30.0, help="Plant spacing.")
    return parser


def main() -> None:
    """Run command-line interface."""
    args = build_parser().parse_args()
    try:
        results = calculate(
            length_m=float(args.length_m),
            width_m=float(args.width_m),
            spacing_cm=float(args.spacing_cm),
        )
    except ValueError as error:
        raise SystemExit(str(error)) from error
    for label, value in results.items():
        print(f"{label}: {value:,.2f}")


if __name__ == "__main__":
    main()
