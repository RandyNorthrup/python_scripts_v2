#!/usr/bin/env python3
"""Estimate annual retirement contributions including employer match."""

from __future__ import annotations

import argparse


def calculate(
    salary: float, employee_percent: float, match_percent: float
) -> dict[str, float]:
    """Calculate and return named results."""
    if salary < 0 or employee_percent < 0 or match_percent < 0:
        error_message = "inputs cannot be negative"
        raise ValueError(error_message)
    return {
        "Employee annual": float(salary * employee_percent / 100),
        "Employer annual": float(salary * match_percent / 100),
        "Combined annual": float(salary * (employee_percent + match_percent) / 100),
    }


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--salary", type=float, default=70000.0, help="Annual salary.")
    parser.add_argument(
        "--employee-percent",
        type=float,
        default=8.0,
        help="Employee contribution percent.",
    )
    parser.add_argument(
        "--match-percent", type=float, default=4.0, help="Employer match percent."
    )
    return parser


def main() -> None:
    """Run command-line interface."""
    args = build_parser().parse_args()
    try:
        results = calculate(
            salary=float(args.salary),
            employee_percent=float(args.employee_percent),
            match_percent=float(args.match_percent),
        )
    except ValueError as error:
        raise SystemExit(str(error)) from error
    for label, value in results.items():
        print(f"{label}: {value:,.2f}")


if __name__ == "__main__":
    main()
