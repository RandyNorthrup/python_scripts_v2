#!/usr/bin/env python3
"""Estimate ideal battery runtime from capacity and device draw."""

from __future__ import annotations

import argparse


def calculate(
    capacity_wh: float, draw_watts: float, efficiency_percent: float
) -> dict[str, float]:
    """Calculate and return named results."""
    if (
        capacity_wh <= 0
        or draw_watts <= 0
        or efficiency_percent <= 0
        or efficiency_percent > 100
    ):
        error_message = "inputs must be positive and efficiency at most 100"
        raise ValueError(error_message)
    return {
        "Usable watt-hours": float(capacity_wh * efficiency_percent / 100),
        "Runtime hours": float(capacity_wh * efficiency_percent / 100 / draw_watts),
    }


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--capacity-wh",
        type=float,
        default=500.0,
        help="Battery capacity in watt-hours.",
    )
    parser.add_argument(
        "--draw-watts", type=float, default=85.0, help="Average device power draw."
    )
    parser.add_argument(
        "--efficiency-percent",
        type=float,
        default=85.0,
        help="Usable efficiency percent.",
    )
    return parser


def main() -> None:
    """Run command-line interface."""
    args = build_parser().parse_args()
    try:
        results = calculate(
            capacity_wh=float(args.capacity_wh),
            draw_watts=float(args.draw_watts),
            efficiency_percent=float(args.efficiency_percent),
        )
    except ValueError as error:
        raise SystemExit(str(error)) from error
    for label, value in results.items():
        print(f"{label}: {value:,.2f}")


if __name__ == "__main__":
    main()
