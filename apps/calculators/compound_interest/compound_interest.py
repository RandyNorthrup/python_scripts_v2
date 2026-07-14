#!/usr/bin/env python3
"""Estimate investment growth with monthly compounding."""

from __future__ import annotations

import argparse


def calculate(principal: float, annual_rate: float, years: float) -> dict[str, float]:
    """Calculate and return named results."""
    if principal < 0 or years < 0:
        error_message = "principal and years cannot be negative"
        raise ValueError(error_message)
    return {
        "Future value": float(principal * (1 + annual_rate / 1200) ** (years * 12)),
        "Interest earned": float(
            principal * (1 + annual_rate / 1200) ** (years * 12) - principal
        ),
    }


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--principal", type=float, default=5000.0, help="Starting balance."
    )
    parser.add_argument(
        "--annual-rate", type=float, default=6.0, help="Annual percentage rate."
    )
    parser.add_argument("--years", type=float, default=10.0, help="Years invested.")
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
