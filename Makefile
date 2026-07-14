.PHONY: catalog format lint test verify

catalog:
	uv run python -m tools.build_catalog
	uv run ruff format apps
	uv run ruff check --fix apps

format:
	uv run ruff format .
	uv run ruff check --fix .

lint:
	uv run ruff format --check .
	uv run ruff check .
	uv run mypy apps tests tools

test:
	uv run pytest

verify: lint test
