#!/usr/bin/env python3
"""Memorize and repeat an expanding digit sequence."""

from __future__ import annotations

import argparse
import random


def run_game(seed: int, *, interactive: bool) -> str:
    """Run game in interactive or automatic demo mode."""
    rng = random.Random(seed)
    sequence = "".join(str(rng.randrange(10)) for _ in range(6))
    if not interactive:
        return f"Study: {sequence}\nCover it and type it from memory."
    print(f"Memorize: {sequence}")
    input("Press Enter when ready.")
    print("\n" * 20)
    guess = input("Sequence: ").strip()
    return "Perfect memory!" if guess == sequence else f"Answer: {sequence}"


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
