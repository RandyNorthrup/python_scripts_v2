#!/usr/bin/env python3
"""Split take-home income into needs, wants, and savings targets."""

from __future__ import annotations

import argparse


def calculate(income: float) -> dict[str, float]:
    """Calculate and return named results."""
    if income < 0:
        error_message = "income cannot be negative"
        raise ValueError(error_message)
    return {
        "Needs": float(income * 0.5),
        "Wants": float(income * 0.3),
        "Savings": float(income * 0.2),
    }


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--income", type=float, default=4000.0, help="Monthly take-home income."
    )
    return parser


def main() -> None:
    """Run command-line interface."""
    args = build_parser().parse_args()
    try:
        results = calculate(
            income=float(args.income),
        )
    except ValueError as error:
        raise SystemExit(str(error)) from error
    for label, value in results.items():
        print(f"{label}: {value:,.2f}")


if __name__ == "__main__":
    main()
