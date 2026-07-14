#!/usr/bin/env python3
"""Estimate monthly payment and total loan cost."""

from __future__ import annotations

import argparse


def calculate(principal: float, annual_rate: float, years: float) -> dict[str, float]:
    """Calculate and return named results."""
    if principal <= 0 or annual_rate <= 0 or years <= 0:
        error_message = "all inputs must be positive"
        raise ValueError(error_message)
    return {
        "Monthly payment": float(
            principal
            * (annual_rate / 1200)
            * (1 + annual_rate / 1200) ** (years * 12)
            / ((1 + annual_rate / 1200) ** (years * 12) - 1)
        ),
        "Total paid": float(
            years
            * 12
            * principal
            * (annual_rate / 1200)
            * (1 + annual_rate / 1200) ** (years * 12)
            / ((1 + annual_rate / 1200) ** (years * 12) - 1)
        ),
    }


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--principal", type=float, default=20000.0, help="Amount borrowed."
    )
    parser.add_argument(
        "--annual-rate", type=float, default=7.0, help="Annual percentage rate."
    )
    parser.add_argument(
        "--years", type=float, default=5.0, help="Loan duration in years."
    )
    return parser


def main() -> None:
    """Run command-line interface."""
    args = build_parser().parse_args()
    try:
        results = calculate(
            principal=float(args.principal),
            annual_rate=float(args.annual_rate),
            years=float(args.years),
        )
    except ValueError as error:
        raise SystemExit(str(error)) from error
    for label, value in results.items():
        print(f"{label}: {value:,.2f}")


if __name__ == "__main__":
    main()
