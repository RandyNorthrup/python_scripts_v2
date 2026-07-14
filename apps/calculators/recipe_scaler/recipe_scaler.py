#!/usr/bin/env python3
"""Scale an ingredient amount between serving counts."""

from __future__ import annotations

import argparse


def calculate(
    amount: float, original_servings: float, new_servings: float
) -> dict[str, float]:
    """Calculate and return named results."""
    if original_servings <= 0 or new_servings <= 0:
        error_message = "servings must be positive"
        raise ValueError(error_message)
    return {
        "Scaled amount": float(amount * new_servings / original_servings),
        "Scale factor": float(new_servings / original_servings),
    }


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--amount", type=float, default=2.5, help="Original ingredient amount."
    )
    parser.add_argument(
        "--original-servings", type=float, default=4.0, help="Original servings."
    )
    parser.add_argument(
        "--new-servings", type=float, default=7.0, help="Desired servings."
    )
    return parser


def main() -> None:
    """Run command-line interface."""
    args = build_parser().parse_args()
    try:
        results = calculate(
            amount=float(args.amount),
            original_servings=float(args.original_servings),
            new_servings=float(args.new_servings),
        )
    except ValueError as error:
        raise SystemExit(str(error)) from error
    for label, value in results.items():
        print(f"{label}: {value:,.2f}")


if __name__ == "__main__":
    main()
