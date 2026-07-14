#!/usr/bin/env python3
"""Estimate paint needed for rectangular walls."""

from __future__ import annotations

import argparse


def calculate(
    wall_width: float, wall_height: float, walls: float, coverage: float, coats: float
) -> dict[str, float]:
    """Calculate and return named results."""
    if wall_width <= 0 or wall_height <= 0 or walls <= 0 or coverage <= 0 or coats <= 0:
        error_message = "all inputs must be positive"
        raise ValueError(error_message)
    return {
        "Area": float(wall_width * wall_height * walls),
        "Liters": float(wall_width * wall_height * walls * coats / coverage),
    }


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--wall-width", type=float, default=4.5, help="Wall width in meters."
    )
    parser.add_argument(
        "--wall-height", type=float, default=2.4, help="Wall height in meters."
    )
    parser.add_argument("--walls", type=float, default=4.0, help="Number of walls.")
    parser.add_argument(
        "--coverage", type=float, default=10.0, help="Square meters per liter."
    )
    parser.add_argument("--coats", type=float, default=2.0, help="Number of coats.")
    return parser


def main() -> None:
    """Run command-line interface."""
    args = build_parser().parse_args()
    try:
        results = calculate(
            wall_width=float(args.wall_width),
            wall_height=float(args.wall_height),
            walls=float(args.walls),
            coverage=float(args.coverage),
            coats=float(args.coats),
        )
    except ValueError as error:
        raise SystemExit(str(error)) from error
    for label, value in results.items():
        print(f"{label}: {value:,.2f}")


if __name__ == "__main__":
    main()
