#!/usr/bin/env python3
"""Take one to three stones; player taking the last stone wins."""

from __future__ import annotations

import argparse
import random


def run_game(seed: int, *, interactive: bool) -> str:
    """Run game in interactive or automatic demo mode."""
    rng = random.Random(seed)
    stones = 15
    lines = []
    while stones > 0:
        if interactive:
            take = int(input(f"{stones} stones. Take 1-3: "))
            if take not in {1, 2, 3} or take > stones:
                return "Invalid move."
        else:
            take = rng.randint(1, min(3, stones))
        stones -= take
        lines.append(f"Player takes {take}; {stones} remain")
        if stones == 0:
            return "\n".join((*lines, "Player wins!"))
        computer = min(stones, 4 - take)
        stones -= computer
        lines.append(f"Computer takes {computer}; {stones} remain")
        if stones == 0:
            return "\n".join((*lines, "Computer wins!"))
    return "\n".join(lines)


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
