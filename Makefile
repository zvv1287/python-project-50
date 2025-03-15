install:
	uv sync

run-gendiff:
	uv run gendiff gendiff/files/file1.json gendiff/files/file2.json

test:
	uv run pytest

lint:
	uv run ruff check

lint-fix:
	uv run ruff check --fix

build:
	uv build

package-install:
	python3 -m pip install --force-reinstall --user dist/*.whl

all-install:build package-install

git-add-commit:
	git status
	git add .
	git commit -m "$m"
	git status



