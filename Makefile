run-h:
	poetry run python3 -m gendiff.scripts.gendiff -h

run-with-files:
	poetry run python3 -m gendiff.scripts.gendiff file1.json file2.json

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 gendiff/


