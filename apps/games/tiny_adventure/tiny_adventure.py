#!/usr/bin/env python3
"""Choose a path through a three-scene text adventure."""

from __future__ import annotations

import argparse
import random


def run_game(seed: int, *, interactive: bool) -> str:
    """Run game in interactive or automatic demo mode."""
    rng = random.Random(seed)
    first = (
        input("Forest or river? ").strip().casefold()
        if interactive
        else rng.choice(("forest", "river"))
    )
    if first == "forest":
        second = (
            input("Climb or listen? ").strip().casefold() if interactive else "listen"
        )
        ending = (
            "You hear the hidden village invite you in."
            if second == "listen"
            else "The old tree shows a road in its rings."
        )
    elif first == "river":
        second = (
            input("Boat or bridge? ").strip().casefold() if interactive else "bridge"
        )
        ending = (
            "The bridge wakes and asks one excellent riddle."
            if second == "bridge"
            else "The boat carries you to tomorrow morning."
        )
    else:
        return "Unknown path."
    return f"Path: {first} -> {second}\n{ending}"


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
