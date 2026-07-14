#!/usr/bin/env python3
"""Estimate weekly and annual commute time."""

from __future__ import annotations

import argparse


def calculate(
    minutes_one_way: float, days_per_week: float, work_weeks: float
) -> dict[str, float]:
    """Calculate and return named results."""
    if minutes_one_way < 0 or days_per_week < 0 or work_weeks < 0:
        error_message = "inputs cannot be negative"
        raise ValueError(error_message)
    return {
        "Weekly hours": float(minutes_one_way * 2 * days_per_week / 60),
        "Annual hours": float(minutes_one_way * 2 * days_per_week * work_weeks / 60),
        "Annual days": float(
            minutes_one_way * 2 * days_per_week * work_weeks / 60 / 24
        ),
    }


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--minutes-one-way", type=float, default=35.0, help="One-way commute minutes."
    )
    parser.add_argument(
        "--days-per-week", type=float, default=5.0, help="Commute days weekly."
    )
    parser.add_argument(
        "--work-weeks", type=float, default=48.0, help="Working weeks yearly."
    )
    return parser


def main() -> None:
    """Run command-line interface."""
    args = build_parser().parse_args()
    try:
        results = calculate(
            minutes_one_way=float(args.minutes_one_way),
            days_per_week=float(args.days_per_week),
            work_weeks=float(args.work_weeks),
        )
    except ValueError as error:
        raise SystemExit(str(error)) from error
    for label, value in results.items():
        print(f"{label}: {value:,.2f}")


if __name__ == "__main__":
    main()
