import json


def to_json(diff: dict):
    return json.dumps(diff, indent=2, sort_keys=True)
