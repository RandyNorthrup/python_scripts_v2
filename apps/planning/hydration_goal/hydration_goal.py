#!/usr/bin/env python3
"""Estimate a simple daily water goal from body weight and activity."""

from __future__ import annotations

import argparse


def calculate(weight_kg: float, activity_minutes: float) -> dict[str, float]:
    """Calculate and return named results."""
    if weight_kg <= 0 or activity_minutes < 0:
        error_message = "weight must be positive and activity nonnegative"
        raise ValueError(error_message)
    return {
        "Base liters": float(weight_kg * 0.033),
        "Activity liters": float(activity_minutes / 30 * 0.35),
        "Total liters": float(weight_kg * 0.033 + activity_minutes / 30 * 0.35),
    }


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--weight-kg", type=float, default=70.0, help="Body weight.")
    parser.add_argument(
        "--activity-minutes", type=float, default=45.0, help="Active minutes."
    )
    return parser


def main() -> None:
    """Run command-line interface."""
    args = build_parser().parse_args()
    try:
        results = calculate(
            weight_kg=float(args.weight_kg),
            activity_minutes=float(args.activity_minutes),
        )
    except ValueError as error:
        raise SystemExit(str(error)) from error
    for label, value in results.items():
        print(f"{label}: {value:,.2f}")


if __name__ == "__main__":
    main()
