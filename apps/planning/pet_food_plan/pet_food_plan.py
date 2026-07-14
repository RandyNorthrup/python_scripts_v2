#!/usr/bin/env python3
"""Estimate food needed and cost over a planning period."""

from __future__ import annotations

import argparse


def calculate(
    grams_per_day: float, days: float, price_per_kg: float
) -> dict[str, float]:
    """Calculate and return named results."""
    if grams_per_day < 0 or days <= 0 or price_per_kg < 0:
        error_message = "days must be positive"
        raise ValueError(error_message)
    return {
        "Food kilograms": float(grams_per_day * days / 1000),
        "Estimated cost": float(grams_per_day * days / 1000 * price_per_kg),
    }


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--grams-per-day", type=float, default=320.0, help="Daily food grams."
    )
    parser.add_argument("--days", type=float, default=30.0, help="Planning days.")
    parser.add_argument(
        "--price-per-kg", type=float, default=8.5, help="Food price per kilogram."
    )
    return parser


def main() -> None:
    """Run command-line interface."""
    args = build_parser().parse_args()
    try:
        results = calculate(
            grams_per_day=float(args.grams_per_day),
            days=float(args.days),
            price_per_kg=float(args.price_per_kg),
        )
    except ValueError as error:
        raise SystemExit(str(error)) from error
    for label, value in results.items():
        print(f"{label}: {value:,.2f}")


if __name__ == "__main__":
    main()
