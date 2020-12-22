ADDED, REMOVED, CHANGED, NO_CHANGED, NESTED, ROOT = \
    'added', 'removed', 'changed', 'no changed', 'nested', 'root'


def add_removed_keys(file1: dict, file2: dict) -> list:
    result = []
    for key in file1.keys() - file2.keys():
        result.append({
            'key': key,
            'type': REMOVED,
            'value': file1[key]
        })
    return result


def add_added_keys(file1: dict, file2: dict) -> list:
    result = []
    for key in file2.keys() - file1.keys():
        result.append({
            'key': key,
            'type': ADDED,
            'value': file2[key]
        })
    return result


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


def add_children(data1: dict, data2: dict) -> list:
    result = []
    result.extend(add_added_keys(data1, data2))
    result.extend(add_removed_keys(data1, data2))

    for key in data1.keys() & data2.keys():
        if data1[key] == data2[key]:
            result.append(add_no_changed_key(key, data2))
        else:
            if isinstance(data1[key], dict) and isinstance(data2[key], dict):
                result.append(add_nested_key(key, data1[key], data2[key]))
            else:
                result.append(add_changed_key(key, data1, data2))
    return sorted(result, key=lambda x: x['key'])


def get_diff(file1: dict, file2: dict) -> dict:
    diff = {
        'type': ROOT,
        'children': add_children(file1, file2)
    }
    return diff
