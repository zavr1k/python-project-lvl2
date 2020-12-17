install:
		@poetry install

build:
		@poetry build

package-install:
		@pip install dist/*.whl

lint:
		@poetry run flake8 gendiff

uninstall:
		@pip uninstall hexlet-code

coverage:
		poetry run coverage run --source=gendiff -m pytest tests
		poetry run coverage xml

test:
		poetry run pytest tests

.PHONY: install lint build package-install
