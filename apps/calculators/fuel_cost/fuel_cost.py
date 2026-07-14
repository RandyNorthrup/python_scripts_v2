#!/usr/bin/env python3
"""Estimate fuel volume and trip cost."""

from __future__ import annotations

import argparse


def calculate(
    distance_km: float, liters_per_100km: float, price_per_liter: float
) -> dict[str, float]:
    """Calculate and return named results."""
    if distance_km < 0 or liters_per_100km < 0 or price_per_liter < 0:
        error_message = "inputs cannot be negative"
        raise ValueError(error_message)
    return {
        "Liters": float(distance_km * liters_per_100km / 100),
        "Trip cost": float(distance_km * liters_per_100km / 100 * price_per_liter),
    }


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--distance-km", type=float, default=450.0, help="Trip distance."
    )
    parser.add_argument(
        "--liters-per-100km", type=float, default=7.2, help="Vehicle consumption."
    )
    parser.add_argument(
        "--price-per-liter", type=float, default=1.65, help="Fuel price."
    )
    return parser


def main() -> None:
    """Run command-line interface."""
    args = build_parser().parse_args()
    try:
        results = calculate(
            distance_km=float(args.distance_km),
            liters_per_100km=float(args.liters_per_100km),
            price_per_liter=float(args.price_per_liter),
        )
    except ValueError as error:
        raise SystemExit(str(error)) from error
    for label, value in results.items():
        print(f"{label}: {value:,.2f}")


if __name__ == "__main__":
    main()
