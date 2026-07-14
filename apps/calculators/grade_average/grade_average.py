#!/usr/bin/env python3
"""Combine two assessment scores using configurable weights."""

from __future__ import annotations

import argparse


def calculate(
    score_a: float, weight_a: float, score_b: float, weight_b: float
) -> dict[str, float]:
    """Calculate and return named results."""
    if weight_a < 0 or weight_b < 0 or weight_a + weight_b <= 0:
        error_message = "weights must have a positive total"
        raise ValueError(error_message)
    return {
        "Weighted grade": float(
            (score_a * weight_a + score_b * weight_b) / (weight_a + weight_b)
        ),
    }


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--score-a", type=float, default=88.0, help="First score.")
    parser.add_argument(
        "--weight-a", type=float, default=40.0, help="First weight percent."
    )
    parser.add_argument("--score-b", type=float, default=94.0, help="Second score.")
    parser.add_argument(
        "--weight-b", type=float, default=60.0, help="Second weight percent."
    )
    return parser


def main() -> None:
    """Run command-line interface."""
    args = build_parser().parse_args()
    try:
        results = calculate(
            score_a=float(args.score_a),
            weight_a=float(args.weight_a),
            score_b=float(args.score_b),
            weight_b=float(args.weight_b),
        )
    except ValueError as error:
        raise SystemExit(str(error)) from error
    for label, value in results.items():
        print(f"{label}: {value:,.2f}")


if __name__ == "__main__":
    main()
