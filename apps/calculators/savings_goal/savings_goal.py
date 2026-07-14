#!/usr/bin/env python3
"""Estimate months needed to reach a savings target."""

from __future__ import annotations

import argparse


def calculate(target: float, current: float, monthly: float) -> dict[str, float]:
    """Calculate and return named results."""
    if target < 0 or current < 0 or monthly <= 0:
        error_message = (
            "target and current cannot be negative; monthly must be positive"
        )
        raise ValueError(error_message)
    return {
        "Amount remaining": float(max(0, target - current)),
        "Months needed": float(max(0, target - current) / monthly),
    }


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", type=float, default=10000.0, help="Savings target.")
    parser.add_argument(
        "--current", type=float, default=1500.0, help="Current savings."
    )
    parser.add_argument(
        "--monthly", type=float, default=450.0, help="Monthly contribution."
    )
    return parser


def main() -> None:
    """Run command-line interface."""
    args = build_parser().parse_args()
    try:
        results = calculate(
            target=float(args.target),
            current=float(args.current),
            monthly=float(args.monthly),
        )
    except ValueError as error:
        raise SystemExit(str(error)) from error
    for label, value in results.items():
        print(f"{label}: {value:,.2f}")


if __name__ == "__main__":
    main()
