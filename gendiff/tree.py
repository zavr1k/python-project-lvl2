ADDED, REMOVED, CHANGED, UNCHANGED, NESTED, ROOT = \
    'added', 'removed', 'changed', 'no changed', 'nested', 'root'


def add_children(file1: dict, file2: dict) -> list:
    result = []
    common_keys = file1.keys() | file2.keys()

    for key in common_keys:
        if key not in file1:
            result.append({
                'key': key,
                'type': ADDED,
                'value': file2[key]
            })
        elif key not in file2:
            result.append({
                'key': key,
                'type': REMOVED,
                'value': file1[key]
            })
        elif file1[key] == file2[key]:
            result.append({
                'key': key,
                'type': UNCHANGED,
                'value': file2[key]
            })
        elif isinstance(file1[key], dict) and isinstance(file2[key], dict):
            result.append({
                'key': key,
                'type': NESTED,
                'children': add_children(file1[key], file2[key])
            })
        else:
            result.append({
                'key': key,
                'type': CHANGED,
                'old_value': file1[key],
                'new_value': file2[key]
            })
    return sorted(result, key=lambda x: x['key'])


def get_diff(file1: dict, file2: dict) -> dict:
    diff = {
        'type': ROOT,
        'children': add_children(file1, file2)
    }
    return diff
