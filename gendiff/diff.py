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


def add_common_key(key: str, file1: dict, file2: dict) -> dict:
    if file1[key] == file2[key]:
        return {
            'key': key,
            'type': NO_CHANGED,
            'value': file2[key]
        }
    elif (isinstance(file1[key], dict) and isinstance(file2[key], dict)) \
            and file1[key] != file2[key]:
        return {
            'key': key,
            'type': NESTED,
            'children': add_children(file1[key], file2[key])
        }
    elif not (isinstance(file1[key], dict) and isinstance(file2[key], dict)) \
            and file1[key] != file2[key]:
        return {
            'key': key,
            'type': CHANGED,
            'old_value': file1[key],
            'new_value': file2[key]
        }


def add_children(data1: dict, data2: dict) -> list:
    result = []
    for key in data2.keys() - data1.keys():
        result.append(add_added_key(key, data2))

    for key in data1.keys() - data2.keys():
        result.append(add_removed_key(key, data1))

    for key in data1.keys() & data2.keys():
        result.append(add_common_key(key, data1, data2))

    return sorted(result, key=lambda x: x['key'])


def get_diff(file1: dict, file2: dict) -> dict:
    diff = {
        'type': ROOT,
        'children': add_children(file1, file2)
    }
    return diff
