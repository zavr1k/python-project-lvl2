import json


def transform(diff: dict):
    return json.dumps(diff, indent=2)
