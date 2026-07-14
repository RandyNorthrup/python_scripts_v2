#!/usr/bin/env python3
"""Compare two package prices using cost per unit."""

from __future__ import annotations

import argparse


def calculate(
    price_a: float, units_a: float, price_b: float, units_b: float
) -> dict[str, float]:
    """Calculate and return named results."""
    if units_a <= 0 or units_b <= 0:
        error_message = "package units must be positive"
        raise ValueError(error_message)
    return {
        "A per unit": float(price_a / units_a),
        "B per unit": float(price_b / units_b),
        "Difference": float(abs(price_a / units_a - price_b / units_b)),
    }


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--price-a", type=float, default=8.49, help="First package price."
    )
    parser.add_argument(
        "--units-a", type=float, default=24.0, help="First package units."
    )
    parser.add_argument(
        "--price-b", type=float, default=6.99, help="Second package price."
    )
    parser.add_argument(
        "--units-b", type=float, default=18.0, help="Second package units."
    )
    return parser


def main() -> None:
    """Run command-line interface."""
    args = build_parser().parse_args()
    try:
        results = calculate(
            price_a=float(args.price_a),
            units_a=float(args.units_a),
            price_b=float(args.price_b),
            units_b=float(args.units_b),
        )
    except ValueError as error:
        raise SystemExit(str(error)) from error
    for label, value in results.items():
        print(f"{label}: {value:,.2f}")


if __name__ == "__main__":
    main()
