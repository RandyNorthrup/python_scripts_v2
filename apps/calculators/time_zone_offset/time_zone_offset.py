#!/usr/bin/env python3
"""Shift a 24-hour clock time by a UTC offset."""

from __future__ import annotations

import argparse


def calculate(hour: float, offset_hours: float) -> dict[str, float]:
    """Calculate and return named results."""
    if hour < 0 or hour >= 24:
        error_message = "hour must be between 0 and 24"
        raise ValueError(error_message)
    return {
        "Shifted hour": float((hour + offset_hours) % 24),
    }


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--hour", type=float, default=14.5, help="Source decimal hour.")
    parser.add_argument(
        "--offset-hours", type=float, default=-7.0, help="Hours to add."
    )
    return parser


def main() -> None:
    """Run command-line interface."""
    args = build_parser().parse_args()
    try:
        results = calculate(
            hour=float(args.hour),
            offset_hours=float(args.offset_hours),
        )
    except ValueError as error:
        raise SystemExit(str(error)) from error
    for label, value in results.items():
        print(f"{label}: {value:,.2f}")


if __name__ == "__main__":
    main()
