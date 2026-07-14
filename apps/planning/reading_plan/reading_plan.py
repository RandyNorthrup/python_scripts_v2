#!/usr/bin/env python3
"""Estimate daily pages and reading time for a deadline."""

from __future__ import annotations

import argparse


def calculate(pages: float, days: float, minutes_per_page: float) -> dict[str, float]:
    """Calculate and return named results."""
    if pages < 0 or days <= 0 or minutes_per_page < 0:
        error_message = "days must be positive"
        raise ValueError(error_message)
    return {
        "Pages per day": float(pages / days),
        "Minutes per day": float(pages / days * minutes_per_page),
    }


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pages", type=float, default=360.0, help="Pages remaining.")
    parser.add_argument("--days", type=float, default=24.0, help="Days available.")
    parser.add_argument(
        "--minutes-per-page", type=float, default=1.5, help="Average reading pace."
    )
    return parser


def main() -> None:
    """Run command-line interface."""
    args = build_parser().parse_args()
    try:
        results = calculate(
            pages=float(args.pages),
            days=float(args.days),
            minutes_per_page=float(args.minutes_per_page),
        )
    except ValueError as error:
        raise SystemExit(str(error)) from error
    for label, value in results.items():
        print(f"{label}: {value:,.2f}")


if __name__ == "__main__":
    main()
