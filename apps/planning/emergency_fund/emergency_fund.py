#!/usr/bin/env python3
"""Estimate emergency-fund target and funding time."""

from __future__ import annotations

import argparse


def calculate(
    monthly_expenses: float, months: float, current: float, monthly_saving: float
) -> dict[str, float]:
    """Calculate and return named results."""
    if monthly_expenses < 0 or months <= 0 or current < 0 or monthly_saving <= 0:
        error_message = "coverage and saving must be positive"
        raise ValueError(error_message)
    return {
        "Target": float(monthly_expenses * months),
        "Gap": float(max(0, monthly_expenses * months - current)),
        "Months to target": float(
            max(0, monthly_expenses * months - current) / monthly_saving
        ),
    }


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--monthly-expenses",
        type=float,
        default=2800.0,
        help="Essential monthly expenses.",
    )
    parser.add_argument("--months", type=float, default=6.0, help="Months of coverage.")
    parser.add_argument("--current", type=float, default=4000.0, help="Current fund.")
    parser.add_argument(
        "--monthly-saving", type=float, default=500.0, help="Monthly contribution."
    )
    return parser


def main() -> None:
    """Run command-line interface."""
    args = build_parser().parse_args()
    try:
        results = calculate(
            monthly_expenses=float(args.monthly_expenses),
            months=float(args.months),
            current=float(args.current),
            monthly_saving=float(args.monthly_saving),
        )
    except ValueError as error:
        raise SystemExit(str(error)) from error
    for label, value in results.items():
        print(f"{label}: {value:,.2f}")


if __name__ == "__main__":
    main()
