#!/usr/bin/env python3
"""Answer a shuffled set of general-knowledge questions."""

from __future__ import annotations

import argparse
import random


def run_game(seed: int, *, interactive: bool) -> str:
    """Run game in interactive or automatic demo mode."""
    rng = random.Random(seed)
    questions = [
        ("Largest ocean?", "pacific"),
        ("How many sides in a hexagon?", "6"),
        ("Planet known as the Red Planet?", "mars"),
    ]
    rng.shuffle(questions)
    if not interactive:
        return "\n".join(
            f"{question} {answer.title()}" for question, answer in questions
        )
    score = sum(
        input(f"{question} ").strip().casefold() == answer
        for question, answer in questions
    )
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
