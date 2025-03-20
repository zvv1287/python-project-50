install:
	uv sync

build:
	uv build

run-gendiff:
	uv run python -m gendiff.scripts.gendiff -h





