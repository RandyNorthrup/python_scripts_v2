#!/usr/bin/env python3
"""Estimate appliance energy use and cost."""

from __future__ import annotations

import argparse


def calculate(
    watts: float, hours_per_day: float, days: float, price_per_kwh: float
) -> dict[str, float]:
    """Calculate and return named results."""
    if watts < 0 or hours_per_day < 0 or days < 0 or price_per_kwh < 0:
        error_message = "inputs cannot be negative"
        raise ValueError(error_message)
    return {
        "Energy kWh": float(watts / 1000 * hours_per_day * days),
        "Cost": float(watts / 1000 * hours_per_day * days * price_per_kwh),
    }


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--watts", type=float, default=900.0, help="Appliance power.")
    parser.add_argument(
        "--hours-per-day", type=float, default=2.0, help="Daily use hours."
    )
    parser.add_argument("--days", type=float, default=30.0, help="Days used.")
    parser.add_argument(
        "--price-per-kwh", type=float, default=0.18, help="Electricity price."
    )
    return parser


def main() -> None:
    """Run command-line interface."""
    args = build_parser().parse_args()
    try:
        results = calculate(
            watts=float(args.watts),
            hours_per_day=float(args.hours_per_day),
            days=float(args.days),
            price_per_kwh=float(args.price_per_kwh),
        )
    except ValueError as error:
        raise SystemExit(str(error)) from error
    for label, value in results.items():
        print(f"{label}: {value:,.2f}")


if __name__ == "__main__":
    main()
