#!/usr/bin/env python3
"""Scale meal portions across people and meals."""

from __future__ import annotations

import argparse


def calculate(grams_per_person: float, people: float, meals: float) -> dict[str, float]:
    """Calculate and return named results."""
    if grams_per_person < 0 or people <= 0 or meals <= 0:
        error_message = "people and meals must be positive"
        raise ValueError(error_message)
    return {
        "Total grams": float(grams_per_person * people * meals),
        "Total kilograms": float(grams_per_person * people * meals / 1000),
    }


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--grams-per-person",
        type=float,
        default=180.0,
        help="Ingredient grams per person.",
    )
    parser.add_argument("--people", type=float, default=5.0, help="People served.")
    parser.add_argument("--meals", type=float, default=2.0, help="Number of meals.")
    return parser


def main() -> None:
    """Run command-line interface."""
    args = build_parser().parse_args()
    try:
        results = calculate(
            grams_per_person=float(args.grams_per_person),
            people=float(args.people),
            meals=float(args.meals),
        )
    except ValueError as error:
        raise SystemExit(str(error)) from error
    for label, value in results.items():
        print(f"{label}: {value:,.2f}")


if __name__ == "__main__":
    main()
