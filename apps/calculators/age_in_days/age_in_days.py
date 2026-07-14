#!/usr/bin/env python3
"""Estimate age in days and hours from years."""

from __future__ import annotations

import argparse


def calculate(years: float) -> dict[str, float]:
    """Calculate and return named results."""
    if years < 0:
        error_message = "years cannot be negative"
        raise ValueError(error_message)
    return {
        "Days": float(years * 365.2425),
        "Hours": float(years * 365.2425 * 24),
    }


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--years", type=float, default=25.0, help="Age in years.")
    return parser


def main() -> None:
    """Run command-line interface."""
    args = build_parser().parse_args()
    try:
        results = calculate(
            years=float(args.years),
        )
    except ValueError as error:
        raise SystemExit(str(error)) from error
    for label, value in results.items():
        print(f"{label}: {value:,.2f}")


if __name__ == "__main__":
    main()
