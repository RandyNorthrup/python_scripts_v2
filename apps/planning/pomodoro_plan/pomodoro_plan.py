#!/usr/bin/env python3
"""Turn work and break intervals into a session timeline."""

from __future__ import annotations

import argparse


def calculate(
    work_minutes: float, break_minutes: float, rounds: float
) -> dict[str, float]:
    """Calculate and return named results."""
    if work_minutes <= 0 or break_minutes < 0 or rounds < 1:
        error_message = "work and rounds must be positive"
        raise ValueError(error_message)
    return {
        "Focus minutes": float(work_minutes * rounds),
        "Break minutes": float(break_minutes * max(0, rounds - 1)),
        "Session minutes": float(
            work_minutes * rounds + break_minutes * max(0, rounds - 1)
        ),
    }


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--work-minutes", type=float, default=25.0, help="Minutes per focus block."
    )
    parser.add_argument(
        "--break-minutes", type=float, default=5.0, help="Minutes per break."
    )
    parser.add_argument("--rounds", type=float, default=4.0, help="Focus rounds.")
    return parser


def main() -> None:
    """Run command-line interface."""
    args = build_parser().parse_args()
    try:
        results = calculate(
            work_minutes=float(args.work_minutes),
            break_minutes=float(args.break_minutes),
            rounds=float(args.rounds),
        )
    except ValueError as error:
        raise SystemExit(str(error)) from error
    for label, value in results.items():
        print(f"{label}: {value:,.2f}")


if __name__ == "__main__":
    main()
