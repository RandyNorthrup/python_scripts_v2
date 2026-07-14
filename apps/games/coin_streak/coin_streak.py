#!/usr/bin/env python3
"""Flip coins until a target run of matching sides appears."""

from __future__ import annotations

import argparse
import random


def run_game(seed: int, *, interactive: bool) -> str:
    """Run game in interactive or automatic demo mode."""
    rng = random.Random(seed)
    target = 4
    previous = ""
    streak = 0
    flips: list[str] = []
    while streak < target:
        if interactive:
            input("Press Enter to flip.")
        current = rng.choice(("H", "T"))
        flips.append(current)
        streak = streak + 1 if current == previous else 1
        previous = current
    return (
        f"Flips: {' '.join(flips)}\n"
        f"Found {target} {previous} in a row after {len(flips)} flips."
    )


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--play", action="store_true", help="Enable interactive play.")
    parser.add_argument("--seed", type=int, default=42, help="Reproducible game seed.")
    return parser


def main() -> None:
    """Run command-line interface."""
    args = build_parser().parse_args()
    print(run_game(int(args.seed), interactive=bool(args.play)))


if __name__ == "__main__":
    main()
