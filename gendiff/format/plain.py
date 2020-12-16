def to_plain(diff: dict, parent=None):
    strings = []
    for key, (status, value) in sorted(diff.items()):
        path = get_whole_path(key, parent)
        if status == "ADDED":
            strings.append(f"Property '{path}' was added with value:"
                           f" {check_value(value)}")
        elif status == "REMOVED":
            strings.append(f"Property '{path}' was removed")
        elif status == "CHANGED":
            strings.append(f"Property '{path}' was updated. "
                           f"From {check_value(value[0])} "
                           f"to {check_value(value[1])}")
        elif status == "NESTED":
            strings.append(to_plain(value, path))
    result = '\n'.join(strings)
    result = result.replace('True', 'true').replace('False', 'false').\
        replace('None', 'null')
    return result


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
