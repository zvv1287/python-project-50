install:
	uv sync

build:
	uv build

run:
	gendiff gendiff/files/file1.json gendiff/files/file2.json

run-yml:
	gendiff gendiff/files/file1.yml gendiff/files/file2.yml

stylish-run:
	gendiff gendiff/files/file1new.json gendiff/files/file2new.json

plain-run:
	gendiff --format plain gendiff/files/file1new.json gendiff/files/file2new.json


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

coverage:
	uv run pytest --cov
