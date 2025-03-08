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

run_gendiff:
	uv run gendiff file1.json file2.json
