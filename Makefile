run:
	poetry run python3 -m gendiff.scripts.gendiff.py -h


build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 gendiff/

install:
	poetry install
