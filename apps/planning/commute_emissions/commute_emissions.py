#!/usr/bin/env python3
"""Estimate travel emissions using a configurable per-kilometer factor."""

from __future__ import annotations

import argparse


def calculate(
    distance_km: float, days: float, kg_co2_per_km: float
) -> dict[str, float]:
    """Calculate and return named results."""
    if distance_km < 0 or days < 0 or kg_co2_per_km < 0:
        error_message = "inputs cannot be negative"
        raise ValueError(error_message)
    return {
        "Annual kilometers": float(distance_km * 2 * days),
        "Annual kg CO2e": float(distance_km * 2 * days * kg_co2_per_km),
    }


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--distance-km", type=float, default=18.0, help="One-way distance."
    )
    parser.add_argument("--days", type=float, default=220.0, help="Commute days.")
    parser.add_argument(
        "--kg-co2-per-km", type=float, default=0.171, help="Emissions factor."
    )
    return parser


def main() -> None:
    """Run command-line interface."""
    args = build_parser().parse_args()
    try:
        results = calculate(
            distance_km=float(args.distance_km),
            days=float(args.days),
            kg_co2_per_km=float(args.kg_co2_per_km),
        )
    except ValueError as error:
        raise SystemExit(str(error)) from error
    for label, value in results.items():
        print(f"{label}: {value:,.2f}")


if __name__ == "__main__":
    main()
