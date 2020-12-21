from gendiff.diff import ADDED, REMOVED, CHANGED, NESTED


def sort_children(children: list) -> list:
    sorted_children = sorted(children, key=lambda x: x['key'])
    return sorted_children


def get_whole_path(key: str, parent: str) -> str:
    if parent:
        return f'{parent}.{key}'
    return key


def check_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, str):
        return f'\'{value}\''
    return value


def to_plain(diff: dict, parent=None):
    strings = []
    sorted_children = sort_children(diff['children'])
    for n in sorted_children:
        path = get_whole_path(n['key'], parent)
        if n['type'] == ADDED:
            strings.append(f"Property '{path}' was added with value:"
                           f" {check_value(n['value'])}")
        elif n['type'] == REMOVED:
            strings.append(f"Property '{path}' was removed")
        elif n['type'] == CHANGED:
            strings.append(f"Property '{path}' was updated. "
                           f"From {check_value(n['old_value'])} "
                           f"to {check_value(n['new_value'])}")
        elif n['type'] == NESTED:
            strings.append(to_plain(n, path))
    result = '\n'.join(strings)
    result = result.replace('True', 'true').replace('False', 'false').\
        replace('None', 'null')
    return result
