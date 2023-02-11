install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=hexlet_python_package --cov-report xml


selfcheck:
	poetry check

check: selfcheck test

build: check
	poetry build

.PHONY: install test lint selfcheck check build
