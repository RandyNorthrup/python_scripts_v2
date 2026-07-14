#!/usr/bin/env python3
"""Estimate sleep duration and cycle count between bedtime and wake time."""

from __future__ import annotations

import argparse


def calculate(bed_hour: float, wake_hour: float) -> dict[str, float]:
    """Calculate and return named results."""
    if bed_hour < 0 or bed_hour >= 24 or wake_hour < 0 or wake_hour >= 24:
        error_message = "hours must be between 0 and 24"
        raise ValueError(error_message)
    return {
        "Sleep hours": float((wake_hour - bed_hour) % 24),
        "Approximate cycles": float(((wake_hour - bed_hour) % 24) * 60 / 90),
    }


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--bed-hour", type=float, default=23.0, help="Bedtime decimal hour."
    )
    parser.add_argument(
        "--wake-hour", type=float, default=7.0, help="Wake decimal hour."
    )
    return parser


def main() -> None:
    """Run command-line interface."""
    args = build_parser().parse_args()
    try:
        results = calculate(
            bed_hour=float(args.bed_hour),
            wake_hour=float(args.wake_hour),
        )
    except ValueError as error:
        raise SystemExit(str(error)) from error
    for label, value in results.items():
        print(f"{label}: {value:,.2f}")


if __name__ == "__main__":
    main()
