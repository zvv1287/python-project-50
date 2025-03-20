install:
	uv sync

build:
	uv build

run-gendiff:
	uv run gendiff gendiff/files/file1.json gendiff/files/file2.json

lint:
	uv run ruff check

lint-fix:
	uv run ruff check --fix

test:
	uv run pytest

s-test:
	uv run pytest -s

check: test lint

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml

