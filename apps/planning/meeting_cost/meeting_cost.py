#!/usr/bin/env python3
"""Estimate labor cost of a meeting."""

from __future__ import annotations

import argparse


def calculate(
    people: float, minutes: float, average_hourly_rate: float
) -> dict[str, float]:
    """Calculate and return named results."""
    if people <= 0 or minutes < 0 or average_hourly_rate < 0:
        error_message = "people must be positive"
        raise ValueError(error_message)
    return {
        "Person-hours": float(people * minutes / 60),
        "Estimated cost": float(people * minutes / 60 * average_hourly_rate),
    }


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--people", type=float, default=6.0, help="Attendee count.")
    parser.add_argument("--minutes", type=float, default=45.0, help="Meeting length.")
    parser.add_argument(
        "--average-hourly-rate",
        type=float,
        default=55.0,
        help="Average loaded hourly cost.",
    )
    return parser


def main() -> None:
    """Run command-line interface."""
    args = build_parser().parse_args()
    try:
        results = calculate(
            people=float(args.people),
            minutes=float(args.minutes),
            average_hourly_rate=float(args.average_hourly_rate),
        )
    except ValueError as error:
        raise SystemExit(str(error)) from error
    for label, value in results.items():
        print(f"{label}: {value:,.2f}")


if __name__ == "__main__":
    main()
