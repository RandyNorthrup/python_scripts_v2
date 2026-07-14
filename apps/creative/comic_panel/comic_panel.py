#!/usr/bin/env python3
"""Create three-beat visual comedy setups for drawing practice."""

from __future__ import annotations

import argparse
import random

PATTERN = "Panel 1: {setup}. Panel 2: {escalation}. Panel 3: {payoff}."
SETUP: tuple[str, ...] = (
    "A cat studies a blueprint",
    "A wizard opens tech support",
    "A robot plants one flower",
    "A knight waits at a laundromat",
)
ESCALATION: tuple[str, ...] = (
    "the blueprint studies back",
    "every caller is a cursed printer",
    "the flower requests an update",
    "the washing machines demand a quest",
)
PAYOFF: tuple[str, ...] = (
    "the cat stamps it approved",
    "the wizard prescribes turning it off and on",
    "the robot offers sunshine as a service",
    "the knight returns with the legendary lost sock",
)


def generate(seed: int, count: int) -> list[str]:
    """Generate reproducible ideas."""
    if count < 1:
        error_message = "count must be at least 1"
        raise ValueError(error_message)
    rng = random.Random(seed)
    return [
        PATTERN.format(
            setup=rng.choice(SETUP),
            escalation=rng.choice(ESCALATION),
            payoff=rng.choice(PAYOFF),
        )
        for _ in range(count)
    ]


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=42, help="Reproducible seed.")
    parser.add_argument("--count", type=int, default=3, help="Number of ideas.")
    return parser


def main() -> None:
    """Run command-line interface."""
    args = build_parser().parse_args()
    try:
        ideas = generate(int(args.seed), int(args.count))
    except ValueError as error:
        raise SystemExit(str(error)) from error
    print("\n".join(f"{index}. {idea}" for index, idea in enumerate(ideas, 1)))


if __name__ == "__main__":
    main()
