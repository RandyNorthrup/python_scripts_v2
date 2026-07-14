#!/usr/bin/env python3
"""Split a restaurant bill with a configurable tip."""

from __future__ import annotations

import argparse


def calculate(subtotal: float, tip_percent: float, people: float) -> dict[str, float]:
    """Calculate and return named results."""
    if subtotal < 0:
        error_message = "subtotal cannot be negative"
        raise ValueError(error_message)
    if people <= 0:
        error_message = "people must be positive"
        raise ValueError(error_message)
    return {
        "Tip": float(subtotal * tip_percent / 100),
        "Total": float(subtotal * (1 + tip_percent / 100)),
        "Per person": float(subtotal * (1 + tip_percent / 100) / people),
    }


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--subtotal", type=float, default=64.0, help="Bill before tip.")
    parser.add_argument("--tip-percent", type=float, default=20.0, help="Tip percent.")
    parser.add_argument(
        "--people", type=float, default=2.0, help="People sharing bill."
    )
    return parser


def main() -> None:
    """Run command-line interface."""
    args = build_parser().parse_args()
    try:
        results = calculate(
            subtotal=float(args.subtotal),
            tip_percent=float(args.tip_percent),
            people=float(args.people),
        )
    except ValueError as error:
        raise SystemExit(str(error)) from error
    for label, value in results.items():
        print(f"{label}: {value:,.2f}")


if __name__ == "__main__":
    main()
