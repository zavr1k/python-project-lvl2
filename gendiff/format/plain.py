from gendiff.tree import ADDED, REMOVED, CHANGED, NESTED, UNCHANGED


def transform(diff: dict) -> str:
    changes = prepares_changes(diff)
    return '\n'.join(changes)


def prepares_changes(node: dict, ancestry='') -> list:
    strings = []
    for child in node["children"]:
        attribute = ancestry + child['key']
        if child['type'] == UNCHANGED:
            continue
        elif child['type'] == NESTED:
            strings.extend(prepares_changes(child, f'{attribute}.'))
        else:
            strings.append(add_row(child, attribute))
    return strings


def add_row(child: dict, attribute: str):
    if child['type'] == ADDED:
        return f"Property '{attribute}' was added with value: " \
               f"{prepare_value(child['value'])}"

    elif child['type'] == REMOVED:
        return f"Property '{attribute}' was removed"

    elif child['type'] == CHANGED:
        return f"Property '{attribute}' was updated. " \
               f"From {prepare_value(child['old_value'])} " \
               f"to {prepare_value(child['new_value'])}"


def prepare_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return f'\'{value}\''
    else:
        return f'{value}'.replace('None', 'null').lower()
