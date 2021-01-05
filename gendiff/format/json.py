import json


def format_json(diff: dict):
    return json.dumps(diff, indent=2)
