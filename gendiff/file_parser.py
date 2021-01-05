import json
import pathlib
import sys

import yaml


def exception_handler(exception_type, exception, traceback):
    print(f"{exception_type.__name__}: {exception}")


sys.excepthook = exception_handler


def get_data(filepath):
    path = get_path(filepath)
    extension = path.suffix
    with path.open() as file:
        if extension == '.json':
            return json.load(file)
        elif extension == '.yml':
            return yaml.safe_load(file)
        else:
            raise ValueError("Unsupported file extension")


def get_path(path):
    based_path = pathlib.Path().cwd()
    absolute_path = based_path.joinpath(path)
    return absolute_path
