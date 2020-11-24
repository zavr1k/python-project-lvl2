install:
	poetry install

build:
	poetry build

package-install:
	pip install --user dist/*.whl

lint:
	poetry run flake8 gendiff

.PHONY install lint build package-install
