#!/usr/bin/env python3
"""Solve five generated arithmetic questions against a timer-free score target."""

from __future__ import annotations

import argparse
import random


def run_game(seed: int, *, interactive: bool) -> str:
    """Run game in interactive or automatic demo mode."""
    rng = random.Random(seed)
    questions = [(rng.randint(2, 12), rng.randint(2, 12)) for _ in range(5)]
    if not interactive:
        return "\n".join(
            f"{left} × {right} = {left * right}" for left, right in questions
        )
    score = 0
    for left, right in questions:
        answer = int(input(f"{left} × {right} = "))
        score += answer == left * right
    return f"Score: {score}/{len(questions)}"


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
