#!/usr/bin/env python3
"""Estimate payoff time without interest using a fixed monthly payment."""

from __future__ import annotations

import argparse


def calculate(balance: float, monthly_payment: float) -> dict[str, float]:
    """Calculate and return named results."""
    if balance < 0 or monthly_payment <= 0:
        error_message = "balance cannot be negative and payment must be positive"
        raise ValueError(error_message)
    return {
        "Months": float(balance / monthly_payment),
        "Years": float(balance / monthly_payment / 12),
    }


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--balance", type=float, default=7500.0, help="Debt balance.")
    parser.add_argument(
        "--monthly-payment", type=float, default=375.0, help="Monthly payment."
    )
    return parser


def main() -> None:
    """Run command-line interface."""
    args = build_parser().parse_args()
    try:
        results = calculate(
            balance=float(args.balance),
            monthly_payment=float(args.monthly_payment),
        )
    except ValueError as error:
        raise SystemExit(str(error)) from error
    for label, value in results.items():
        print(f"{label}: {value:,.2f}")


if __name__ == "__main__":
    main()
