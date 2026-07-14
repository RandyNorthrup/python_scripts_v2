#!/usr/bin/env python3
"""Convert Celsius into Fahrenheit and Kelvin."""

from __future__ import annotations

import argparse


def calculate(celsius: float) -> dict[str, float]:
    """Calculate and return named results."""
    if celsius < -273.15:
        error_message = "temperature cannot be below absolute zero"
        raise ValueError(error_message)
    return {
        "Fahrenheit": float(celsius * 9 / 5 + 32),
        "Kelvin": float(celsius + 273.15),
    }


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--celsius", type=float, default=22.0, help="Temperature in Celsius."
    )
    return parser


def main() -> None:
    """Run command-line interface."""
    args = build_parser().parse_args()
    try:
        results = calculate(
            celsius=float(args.celsius),
        )
    except ValueError as error:
        raise SystemExit(str(error)) from error
    for label, value in results.items():
        print(f"{label}: {value:,.2f}")


if __name__ == "__main__":
    main()
