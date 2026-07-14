#!/usr/bin/env python3
"""Calculate body mass index from metric measurements."""

from __future__ import annotations

import argparse


def calculate(weight_kg: float, height_cm: float) -> dict[str, float]:
    """Calculate and return named results."""
    if weight_kg <= 0 or height_cm <= 0:
        error_message = "weight and height must be positive"
        raise ValueError(error_message)
    return {
        "BMI": float(weight_kg / (height_cm / 100) ** 2),
    }


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--weight-kg", type=float, default=72.0, help="Weight in kilograms."
    )
    parser.add_argument(
        "--height-cm", type=float, default=175.0, help="Height in centimeters."
    )
    return parser


def main() -> None:
    """Run command-line interface."""
    args = build_parser().parse_args()
    try:
        results = calculate(
            weight_kg=float(args.weight_kg),
            height_cm=float(args.height_cm),
        )
    except ValueError as error:
        raise SystemExit(str(error)) from error
    for label, value in results.items():
        print(f"{label}: {value:,.2f}")


if __name__ == "__main__":
    main()
