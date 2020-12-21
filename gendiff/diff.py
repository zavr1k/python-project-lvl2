ADDED, REMOVED, CHANGED, NO_CHANGED, NESTED, ROOT = \
    'added', 'removed', 'changed', 'no changed', 'nested', 'root'


def add_removed_key(key: str, file: dict) -> dict:
    return {
        'key': key,
        'type': REMOVED,
        'value': file[key]
    }


def add_added_key(key: str, file: dict) -> dict:
    return {
        'key': key,
        'type': ADDED,
        'value': file[key]
    }


def add_no_changed_key(key: str, file: dict) -> dict:
    return {
        'key': key,
        'type': NO_CHANGED,
        'value': file[key]
    }


def add_changed_key(key: str, file1: dict, file2: dict) -> dict:
    return {
        'key': key,
        'type': CHANGED,
        'old_value': file1[key],
        'new_value': file2[key]
    }


def add_nested_key(key: str, file1: dict, file2: dict) -> dict:
    return {
        'key': key,
        'type': NESTED,
        'children': add_children(file1, file2)
    }


def add_children(data1: dict, data2: dict):
    result = []

    for key in data2.keys() - data1.keys():
        result.append(add_added_key(key, data2))

    for key in data1.keys() - data2.keys():
        result.append(add_removed_key(key, data1))

    for key in data1.keys() & data2.keys():
        if data1[key] == data2[key]:
            result.append(add_no_changed_key(key, data2))
        else:
            if isinstance(data1[key], dict) and isinstance(data2[key], dict):
                result.append(add_nested_key(key, data1[key], data2[key]))
            else:
                result.append(add_changed_key(key, data1, data2))
    return result


def get_diff(file1: dict, file2: dict) -> dict:
    diff = {
        'type': ROOT,
        'children': add_children(file1, file2)
    }
    return diff
