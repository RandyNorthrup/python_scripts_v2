#!/usr/bin/env python3
"""Allocate study time evenly across subjects and days."""

from __future__ import annotations

import argparse


def calculate(total_hours: float, subjects: float, days: float) -> dict[str, float]:
    """Calculate and return named results."""
    if total_hours < 0 or subjects <= 0 or days <= 0:
        error_message = "subjects and days must be positive"
        raise ValueError(error_message)
    return {
        "Hours per subject": float(total_hours / subjects),
        "Hours per day": float(total_hours / days),
        "Minutes per subject per day": float(total_hours * 60 / subjects / days),
    }


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--total-hours", type=float, default=12.0, help="Total study hours."
    )
    parser.add_argument("--subjects", type=float, default=3.0, help="Subject count.")
    parser.add_argument("--days", type=float, default=6.0, help="Study days.")
    return parser


def main() -> None:
    """Run command-line interface."""
    args = build_parser().parse_args()
    try:
        results = calculate(
            total_hours=float(args.total_hours),
            subjects=float(args.subjects),
            days=float(args.days),
        )
    except ValueError as error:
        raise SystemExit(str(error)) from error
    for label, value in results.items():
        print(f"{label}: {value:,.2f}")


if __name__ == "__main__":
    main()
