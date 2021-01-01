from gendiff.tree import ADDED, REMOVED, CHANGED, UNCHANGED, NESTED


def prepare(value, indent):
    if isinstance(value, dict):
        return prepare_dict(value, indent)
    else:
        return str(value).replace('True', 'true').replace('False', 'false').\
            replace('None', 'null')


def prepare_dict(value, indent):
    spacer = ' ' * (indent + 6)
    result = '{\n'
    for key, value in value.items():
        if isinstance(value, dict):
            result += f'{spacer}{key}: {prepare(value, indent + 4)}\n'
        else:
            result += f'{spacer}{key}: {value}\n'
    else:
        result += f'{spacer[4:]}' + '}'
    return result


def transform(diff: dict, indent=2):
    spacer = ' ' * indent
    result = '{\n'
    for n in diff['children']:
        if n['type'] == ADDED:
            result += f'{spacer}+ {n["key"]}: {prepare(n["value"], indent)}\n'
        elif n['type'] == REMOVED:
            result += f'{spacer}- {n["key"]}: {prepare(n["value"], indent)}\n'
        elif n['type'] == CHANGED:
            result += \
                f'{spacer}- {n["key"]}: {prepare(n["old_value"], indent)}\n'
            result += \
                f'{spacer}+ {n["key"]}: {prepare(n["new_value"], indent)}\n'
        elif n['type'] == UNCHANGED:
            result += f'{spacer}  {n["key"]}: {prepare(n["value"], indent)}\n'
        elif n['type'] == NESTED:
            result += \
                f'{spacer}  {n["key"]}: {transform(n, indent=indent + 4)}\n'
    result += f'{spacer[2:]}' + '}'
    return result
