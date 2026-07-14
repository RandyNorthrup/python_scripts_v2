#!/usr/bin/env python3
"""Estimate total trip cost from daily and fixed expenses."""

from __future__ import annotations

import argparse


def calculate(
    days: float,
    lodging_per_day: float,
    food_per_day: float,
    transport: float,
    buffer_percent: float,
) -> dict[str, float]:
    """Calculate and return named results."""
    if days <= 0 or min(lodging_per_day, food_per_day, transport, buffer_percent) < 0:
        error_message = "costs cannot be negative"
        raise ValueError(error_message)
    return {
        "Base cost": float(days * (lodging_per_day + food_per_day) + transport),
        "Buffer": float(
            (days * (lodging_per_day + food_per_day) + transport) * buffer_percent / 100
        ),
        "Total budget": float(
            (days * (lodging_per_day + food_per_day) + transport)
            * (1 + buffer_percent / 100)
        ),
    }


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--days", type=float, default=7.0, help="Trip days.")
    parser.add_argument(
        "--lodging-per-day", type=float, default=120.0, help="Daily lodging."
    )
    parser.add_argument("--food-per-day", type=float, default=55.0, help="Daily food.")
    parser.add_argument(
        "--transport", type=float, default=350.0, help="Fixed transport."
    )
    parser.add_argument(
        "--buffer-percent", type=float, default=10.0, help="Contingency percent."
    )
    return parser


def main() -> None:
    """Run command-line interface."""
    args = build_parser().parse_args()
    try:
        results = calculate(
            days=float(args.days),
            lodging_per_day=float(args.lodging_per_day),
            food_per_day=float(args.food_per_day),
            transport=float(args.transport),
            buffer_percent=float(args.buffer_percent),
        )
    except ValueError as error:
        raise SystemExit(str(error)) from error
    for label, value in results.items():
        print(f"{label}: {value:,.2f}")


if __name__ == "__main__":
    main()
