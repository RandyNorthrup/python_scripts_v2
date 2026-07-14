#!/usr/bin/env python3
"""Convert race distance and finish time into running pace."""

from __future__ import annotations

import argparse


def calculate(distance_km: float, minutes: float) -> dict[str, float]:
    """Calculate and return named results."""
    if distance_km <= 0 or minutes <= 0:
        error_message = "distance and time must be positive"
        raise ValueError(error_message)
    return {
        "Minutes per kilometer": float(minutes / distance_km),
        "Kilometers per hour": float(distance_km / (minutes / 60)),
    }


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--distance-km", type=float, default=10.0, help="Distance in kilometers."
    )
    parser.add_argument(
        "--minutes", type=float, default=52.0, help="Finish time in minutes."
    )
    return parser


def main() -> None:
    """Run command-line interface."""
    args = build_parser().parse_args()
    try:
        results = calculate(
            distance_km=float(args.distance_km),
            minutes=float(args.minutes),
        )
    except ValueError as error:
        raise SystemExit(str(error)) from error
    for label, value in results.items():
        print(f"{label}: {value:,.2f}")


if __name__ == "__main__":
    main()
