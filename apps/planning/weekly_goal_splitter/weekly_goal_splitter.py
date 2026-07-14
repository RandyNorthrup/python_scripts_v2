#!/usr/bin/env python3
"""Break a measurable goal into weekday and weekend targets."""

from __future__ import annotations

import argparse


def calculate(goal: float, weekday_percent: float) -> dict[str, float]:
    """Calculate and return named results."""
    if goal < 0 or weekday_percent < 0 or weekday_percent > 100:
        error_message = "percent must be between 0 and 100"
        raise ValueError(error_message)
    return {
        "Weekday total": float(goal * weekday_percent / 100),
        "Per weekday": float(goal * weekday_percent / 100 / 5),
        "Per weekend day": float(goal * (1 - weekday_percent / 100) / 2),
    }


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--goal", type=float, default=100.0, help="Weekly target units."
    )
    parser.add_argument(
        "--weekday-percent",
        type=float,
        default=70.0,
        help="Percent assigned to weekdays.",
    )
    return parser


def main() -> None:
    """Run command-line interface."""
    args = build_parser().parse_args()
    try:
        results = calculate(
            goal=float(args.goal),
            weekday_percent=float(args.weekday_percent),
        )
    except ValueError as error:
        raise SystemExit(str(error)) from error
    for label, value in results.items():
        print(f"{label}: {value:,.2f}")


if __name__ == "__main__":
    main()
