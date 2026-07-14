# Sleep Cycle Planner

Estimate sleep duration and cycle count between bedtime and wake time.

## What it does

This standalone Python 3 command-line app runs with a useful built-in demo when no arguments are supplied. It uses clear text output, no color-only meaning, and keyboard-only controls where interaction is available.

## How to use it

```bash
python3 sleep_cycle_planner.py
python3 sleep_cycle_planner.py --bed-hour 28.75
```

Run `python3 sleep_cycle_planner.py --help` for every option. Interactive quizzes and games only prompt when `--play` is supplied.

## How to modify it

Edit `calculate()` to add formulas, then add matching CLI inputs in `build_parser()`. The file is self-contained, so you can copy this directory anywhere with Python 3.11 or newer.

After an edit, run repository checks from the project root:

```bash
make verify
```

## Requirements

- Python 3.11 or newer
- No third-party runtime packages

`requirements.txt` is intentionally empty except for a comment because this app uses only the Python standard library.
