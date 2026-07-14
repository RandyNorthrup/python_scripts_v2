#!/usr/bin/env python3
"""Measure absolute and percentage change between values."""

from __future__ import annotations

import argparse


def calculate(old_value: float, new_value: float) -> dict[str, float]:
    """Calculate and return named results."""
    if old_value == 0:
        error_message = "old value cannot be zero"
        raise ValueError(error_message)
    return {
        "Absolute change": float(new_value - old_value),
        "Percentage change": float((new_value - old_value) / abs(old_value) * 100),
    }


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--old-value", type=float, default=80.0, help="Starting value.")
    parser.add_argument("--new-value", type=float, default=92.0, help="Ending value.")
    return parser


def main() -> None:
    """Run command-line interface."""
    args = build_parser().parse_args()
    try:
        results = calculate(
            old_value=float(args.old_value),
            new_value=float(args.new_value),
        )
    except ValueError as error:
        raise SystemExit(str(error)) from error
    for label, value in results.items():
        print(f"{label}: {value:,.2f}")


if __name__ == "__main__":
    main()
