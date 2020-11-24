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

.PHONY: install lint build package-install
