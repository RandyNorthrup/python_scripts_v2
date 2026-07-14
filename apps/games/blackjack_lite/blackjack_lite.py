#!/usr/bin/env python3
"""Play a simplified hit-or-stand blackjack hand."""

from __future__ import annotations

import argparse
import random


def run_game(seed: int, *, interactive: bool) -> str:
    """Run game in interactive or automatic demo mode."""
    rng = random.Random(seed)
    deck = [min(rank, 10) for rank in range(1, 14) for _ in range(4)]
    rng.shuffle(deck)
    player = [deck.pop(), deck.pop()]
    dealer = [deck.pop(), deck.pop()]
    while (
        sum(player) < 21
        and interactive
        and input(f"Hand {player} ({sum(player)}). Hit? [y/N] ").casefold() == "y"
    ):
        player.append(deck.pop())
    while sum(dealer) < 17:
        dealer.append(deck.pop())
    player_total, dealer_total = sum(player), sum(dealer)
    if player_total > 21:
        result = "bust"
    elif dealer_total > 21 or player_total > dealer_total:
        result = "win"
    elif player_total == dealer_total:
        result = "push"
    else:
        result = "lose"
    return (
        f"Your hand: {player} = {player_total}\n"
        f"Dealer: {dealer} = {dealer_total}\n"
        f"Result: {result}"
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
