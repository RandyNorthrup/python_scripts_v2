"""Build standalone apps, documentation, and machine-readable catalog."""

from __future__ import annotations

import json
from pathlib import Path

from tools.catalog_models import (
    AppSpec,
    FileApp,
    FormulaApp,
    GameApp,
    GeneratorApp,
    QuizApp,
    TextApp,
)
from tools.catalog_renderers import render_app
from tools.catalog_specs import ALL_APPS

ROOT = Path(__file__).resolve().parents[1]
APPS_ROOT = ROOT / "apps"
EXPECTED_APP_COUNT = 162


def usage_for(app: AppSpec) -> str:
    """Return type-specific usage examples."""
    command = f"python3 {app.slug}.py"
    if isinstance(app, FormulaApp):
        first = app.parameters[0]
        return f"{command}\n{command} --{first.name.replace('_', '-')} {first.default * 1.25:g}"
    if isinstance(app, TextApp):
        return f'{command}\n{command} "your input here"'
    if isinstance(app, GeneratorApp):
        return f"{command}\n{command} --seed 7 --count 5"
    if isinstance(app, QuizApp | GameApp):
        return f"{command}\n{command} --play --seed 7"
    if isinstance(app, FileApp):
        return f"{command}\n{command} /path/to/file-or-directory"
    raise TypeError(type(app).__name__)


def modification_hint(app: AppSpec) -> str:
    """Return safe extension point for an app type."""
    if isinstance(app, FormulaApp):
        return "Edit `calculate()` to add formulas, then add matching CLI inputs in `build_parser()`."
    if isinstance(app, TextApp):
        return "Edit `transform()` to change the text rule; keep it pure so it remains easy to test."
    if isinstance(app, GeneratorApp):
        return "Extend the word-bank constants or change `PATTERN`; pass a seed to reproduce output."
    if isinstance(app, QuizApp):
        return "Add `(question, answer, explanation)` tuples to `CARDS`; normalized answers ignore case and extra spaces."
    if isinstance(app, GameApp):
        return "Edit `run_game()` to change rules; preserve noninteractive demo mode for automated checks."
    if isinstance(app, FileApp):
        return "Edit `inspect_path()` to add analysis. Keep the tool read-only unless its name and documentation clearly announce writes."
    raise TypeError(type(app).__name__)


def render_readme(app: AppSpec) -> str:
    """Render one app's usage and modification guide."""
    return f"""# {app.title}

{app.summary}

## What it does

This standalone Python 3 command-line app runs with a useful built-in demo when no arguments are supplied. It uses clear text output, no color-only meaning, and keyboard-only controls where interaction is available.

## How to use it

```bash
{usage_for(app)}
```

Run `python3 {app.slug}.py --help` for every option. Interactive quizzes and games only prompt when `--play` is supplied.

## How to modify it

{modification_hint(app)} The file is self-contained, so you can copy this directory anywhere with Python 3.11 or newer.

After an edit, run repository checks from the project root:

```bash
make verify
```

## Requirements

- Python 3.11 or newer
- No third-party runtime packages

`requirements.txt` is intentionally empty except for a comment because this app uses only the Python standard library.
"""


def build_manifest(apps: tuple[AppSpec, ...]) -> list[dict[str, str]]:
    """Build serializable app inventory."""
    return [
        {
            "category": app.category,
            "slug": app.slug,
            "title": app.title,
            "summary": app.summary,
            "script": f"apps/{app.category}/{app.slug}/{app.slug}.py",
        }
        for app in sorted(apps, key=lambda item: (item.category, item.slug))
    ]


def render_root_readme(manifest: list[dict[str, str]]) -> str:
    """Render repository overview and linked catalog."""
    categories = sorted({item["category"] for item in manifest})
    sections: list[str] = []
    for category in categories:
        label = category.replace("_", " ").title()
        rows = [
            f"- [{item['title']}]({Path(item['script']).parent.as_posix()}/README.md) — {item['summary']}"
            for item in manifest
            if item["category"] == category
        ]
        sections.append(f"## {label}\n\n" + "\n".join(rows))
    catalog_sections = "\n\n".join(sections)
    return f"""# Python Scripts V2

Curated collection of **{len(manifest)} standalone Python 3 apps**. Every app has one Python file, its own README, and its own `requirements.txt`. Categories balance useful utilities, learning exercises, creative prompts, and playable terminal games.

## Quick start

```bash
python3 apps/calculators/tip_calculator/tip_calculator.py
python3 apps/games/number_guess/number_guess.py --play
```

No app needs third-party runtime packages. Each defaults to a safe, noninteractive demo. Filesystem tools are read-only.

## Development

```bash
uv sync
make verify
```

Quality gates use Ruff with every rule family enabled, narrow documented exclusions, strict mypy, structural contract checks, and one smoke-test case per app.

## Repository layout

```text
apps/<category>/<app>/<app>.py
apps/<category>/<app>/README.md
apps/<category>/<app>/requirements.txt
tests/test_catalog.py
tools/build_catalog.py
catalog.json
```

`catalog.json` is the machine-readable index. Regenerate and format checked-in app files and docs with `make catalog`.

## App catalog

{catalog_sections}

## Safety and accessibility

Apps avoid network calls, destructive filesystem changes, animation, color-only status, and mouse-only input. Terminal output stays readable at narrow widths; interactive apps accept keyboard input and also offer noninteractive demos.

## License

MIT. See `LICENSE`.
"""


def validate_specs(apps: tuple[AppSpec, ...]) -> None:
    """Reject incomplete or duplicated catalog specifications."""
    if len(apps) != EXPECTED_APP_COUNT:
        message = f"expected {EXPECTED_APP_COUNT} apps, found {len(apps)}"
        raise ValueError(message)
    keys = [(app.category, app.slug) for app in apps]
    if len(keys) != len(set(keys)):
        message = "duplicate category/slug in catalog"
        raise ValueError(message)
    for app in apps:
        if not app.slug.replace("_", "").isalnum() or app.slug.casefold() != app.slug:
            message = f"invalid slug: {app.slug}"
            raise ValueError(message)


def build() -> None:
    """Write all generated catalog artifacts."""
    validate_specs(ALL_APPS)
    manifest = build_manifest(ALL_APPS)
    for app in ALL_APPS:
        directory = APPS_ROOT / app.category / app.slug
        directory.mkdir(parents=True, exist_ok=True)
        script_path = directory / f"{app.slug}.py"
        script_path.write_text(render_app(app), encoding="utf-8")
        script_path.chmod(0o755)
        (directory / "README.md").write_text(render_readme(app), encoding="utf-8")
        (directory / "requirements.txt").write_text(
            "# Standard library only; no third-party packages required.\n",
            encoding="utf-8",
        )
    (ROOT / "catalog.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    (ROOT / "README.md").write_text(render_root_readme(manifest), encoding="utf-8")


if __name__ == "__main__":
    build()
