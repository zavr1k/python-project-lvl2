import json
import yaml


def get_data(file, extension):
    with file.open() as file:
        if extension == ".json":
            return json.load(file)
        elif extension == ".yml":
            return yaml.safe_load(file)
        else:
            raise ValueError("Unsupported file extension")
