#!/usr/bin/env python3
"""Find sales volume needed to cover fixed costs."""

from __future__ import annotations

import argparse


def calculate(
    fixed_cost: float, price: float, variable_cost: float
) -> dict[str, float]:
    """Calculate and return named results."""
    if fixed_cost < 0 or price <= variable_cost:
        error_message = "price must exceed variable cost"
        raise ValueError(error_message)
    return {
        "Break-even units": float(fixed_cost / (price - variable_cost)),
        "Contribution margin": float(price - variable_cost),
    }


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--fixed-cost", type=float, default=12000.0, help="Fixed costs."
    )
    parser.add_argument(
        "--price", type=float, default=45.0, help="Sale price per unit."
    )
    parser.add_argument(
        "--variable-cost", type=float, default=18.0, help="Variable cost per unit."
    )
    return parser


def main() -> None:
    """Run command-line interface."""
    args = build_parser().parse_args()
    try:
        results = calculate(
            fixed_cost=float(args.fixed_cost),
            price=float(args.price),
            variable_cost=float(args.variable_cost),
        )
    except ValueError as error:
        raise SystemExit(str(error)) from error
    for label, value in results.items():
        print(f"{label}: {value:,.2f}")


if __name__ == "__main__":
    main()
