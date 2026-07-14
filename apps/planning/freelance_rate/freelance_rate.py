#!/usr/bin/env python3
"""Estimate an hourly freelance rate from income and overhead goals."""

from __future__ import annotations

import argparse


def calculate(
    annual_income: float, billable_hours: float, overhead_percent: float
) -> dict[str, float]:
    """Calculate and return named results."""
    if annual_income < 0 or billable_hours <= 0 or overhead_percent < 0:
        error_message = "hours must be positive"
        raise ValueError(error_message)
    return {
        "Base hourly": float(annual_income / billable_hours),
        "Target hourly": float(
            annual_income / billable_hours * (1 + overhead_percent / 100)
        ),
    }


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--annual-income", type=float, default=80000.0, help="Desired personal income."
    )
    parser.add_argument(
        "--billable-hours", type=float, default=1200.0, help="Annual billable hours."
    )
    parser.add_argument(
        "--overhead-percent",
        type=float,
        default=25.0,
        help="Business overhead percent.",
    )
    return parser


def main() -> None:
    """Run command-line interface."""
    args = build_parser().parse_args()
    try:
        results = calculate(
            annual_income=float(args.annual_income),
            billable_hours=float(args.billable_hours),
            overhead_percent=float(args.overhead_percent),
        )
    except ValueError as error:
        raise SystemExit(str(error)) from error
    for label, value in results.items():
        print(f"{label}: {value:,.2f}")


if __name__ == "__main__":
    main()
