import json
import pathlib

import yaml


def get_data(filepath):
    path = get_path(filepath)
    extension = path.suffix
    with path.open() as file:
        if extension == '.json':
            content = json.load(file)
        elif extension == '.yml':
            content = yaml.safe_load(file)
    return content


def get_path(path):
    based_path = pathlib.Path().cwd()
    absolute_path = based_path.joinpath(path)
    return absolute_path
