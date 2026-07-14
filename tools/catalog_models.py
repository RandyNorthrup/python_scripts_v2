"""Typed models used by catalog generator."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Parameter:
    """One numeric command-line input."""

    name: str
    default: float
    help_text: str


@dataclass(frozen=True)
class FormulaApp:
    """Numeric app generated from named inputs and result expressions."""

    category: str
    slug: str
    title: str
    summary: str
    parameters: tuple[Parameter, ...]
    outputs: tuple[tuple[str, str], ...]
    validations: tuple[tuple[str, str], ...] = ()


@dataclass(frozen=True)
class TextApp:
    """Text-processing app generated from a typed function body."""

    category: str
    slug: str
    title: str
    summary: str
    default_text: str
    body: str
    imports: tuple[str, ...] = ()


@dataclass(frozen=True)
class GeneratorApp:
    """Seeded creative generator built from interchangeable word banks."""

    category: str
    slug: str
    title: str
    summary: str
    pattern: str
    banks: tuple[tuple[str, tuple[str, ...]], ...]


@dataclass(frozen=True)
class QuizApp:
    """Interactive educational quiz with a noninteractive study mode."""

    category: str
    slug: str
    title: str
    summary: str
    cards: tuple[tuple[str, str, str], ...]


@dataclass(frozen=True)
class FileApp:
    """Read-only file or directory analysis app."""

    category: str
    slug: str
    title: str
    summary: str
    body: str
    imports: tuple[str, ...] = ()


@dataclass(frozen=True)
class GameApp:
    """Small terminal game with interactive and demo modes."""

    category: str
    slug: str
    title: str
    summary: str
    body: str
    imports: tuple[str, ...] = ()


AppSpec = FormulaApp | TextApp | GeneratorApp | QuizApp | FileApp | GameApp
