#!/usr/bin/env python3
"""Estimate table count and floor-space needs for an event."""

from __future__ import annotations

import argparse


def calculate(
    guests: float, seats_per_table: float, square_meters_per_guest: float
) -> dict[str, float]:
    """Calculate and return named results."""
    if guests <= 0 or seats_per_table <= 0 or square_meters_per_guest <= 0:
        error_message = "all inputs must be positive"
        raise ValueError(error_message)
    return {
        "Tables": float(guests / seats_per_table),
        "Floor area square meters": float(guests * square_meters_per_guest),
    }


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--guests", type=float, default=120.0, help="Expected guests.")
    parser.add_argument(
        "--seats-per-table", type=float, default=8.0, help="Seats at each table."
    )
    parser.add_argument(
        "--square-meters-per-guest",
        type=float,
        default=1.5,
        help="Floor area per guest.",
    )
    return parser


def main() -> None:
    """Run command-line interface."""
    args = build_parser().parse_args()
    try:
        results = calculate(
            guests=float(args.guests),
            seats_per_table=float(args.seats_per_table),
            square_meters_per_guest=float(args.square_meters_per_guest),
        )
    except ValueError as error:
        raise SystemExit(str(error)) from error
    for label, value in results.items():
        print(f"{label}: {value:,.2f}")


if __name__ == "__main__":
    main()
