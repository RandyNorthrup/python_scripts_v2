#!/usr/bin/env python3
"""Inspect an IPv4 or IPv6 network in CIDR notation."""

from __future__ import annotations

import argparse
import ipaddress

DEFAULT_TEXT = "192.168.10.42/24"


def transform(text: str) -> str:
    """Transform or analyze input text."""
    interface = ipaddress.ip_interface(text.strip())
    network = interface.network
    return (
        f"Address: {interface.ip}\n"
        f"Network: {network}\n"
        f"Addresses: {network.num_addresses}\n"
        f"Private: {interface.ip.is_private}"
    )


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "text",
        nargs="?",
        default=DEFAULT_TEXT,
        help="Text to process.",
    )
    return parser


def main() -> None:
    """Run command-line interface."""
    args = build_parser().parse_args()
    print(transform(str(args.text)))


if __name__ == "__main__":
    main()
