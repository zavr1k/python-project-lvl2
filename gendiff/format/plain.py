from gendiff.tree import ADDED, REMOVED, CHANGED, NESTED, UNCHANGED


def to_plain(diff: dict) -> str:
    changes = add_children(diff['children'])
    return '\n'.join(changes)


def add_children(children: list, ancestry=None) -> list:
    strings = []
    for child in children:
        if ancestry is None:
            attribute = child['key']
        else:
            attribute = f'{ancestry}.{child["key"]}'

        if child['type'] == UNCHANGED:
            continue
        elif child['type'] == NESTED:
            strings.extend(add_children(child["children"], attribute))
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
    elif isinstance(value, bool):
        return f'{value}'.lower()
    elif isinstance(value, int):
        return str(int)
    else:
        return 'null'
