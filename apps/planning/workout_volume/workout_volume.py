#!/usr/bin/env python3
"""Calculate resistance-training volume from sets, reps, and weight."""

from __future__ import annotations

import argparse


def calculate(
    sets: float, reps: float, weight_kg: float, exercises: float
) -> dict[str, float]:
    """Calculate and return named results."""
    if sets <= 0 or reps <= 0 or weight_kg < 0 or exercises <= 0:
        error_message = "counts must be positive"
        raise ValueError(error_message)
    return {
        "Total repetitions": float(sets * reps * exercises),
        "Training volume kg": float(sets * reps * weight_kg * exercises),
    }


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sets", type=float, default=4.0, help="Set count.")
    parser.add_argument("--reps", type=float, default=8.0, help="Repetitions per set.")
    parser.add_argument(
        "--weight-kg", type=float, default=60.0, help="Weight per repetition."
    )
    parser.add_argument("--exercises", type=float, default=3.0, help="Exercise count.")
    return parser


def main() -> None:
    """Run command-line interface."""
    args = build_parser().parse_args()
    try:
        results = calculate(
            sets=float(args.sets),
            reps=float(args.reps),
            weight_kg=float(args.weight_kg),
            exercises=float(args.exercises),
        )
    except ValueError as error:
        raise SystemExit(str(error)) from error
    for label, value in results.items():
        print(f"{label}: {value:,.2f}")


if __name__ == "__main__":
    main()
