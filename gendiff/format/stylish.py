def stylish(diff: dict, indent=2) -> str:
    spacer = ' ' * indent
    result = '{\n'
    for key, (status, value) in sorted(diff.items()):
        if status == 'ADDED':
            result += f'{spacer}+ {key}: {prepare(value, indent)}\n'
        elif status == 'REMOVED':
            result += f'{spacer}- {key}: {prepare(value, indent)}\n'
        elif status == 'CHANGED':
            result += f'{spacer}- {key}: {prepare(value[0], indent)}\n'
            result += f'{spacer}+ {key}: {prepare(value[1], indent)}\n'
        elif status == 'NO_CHANGED':
            result += f'{spacer}  {key}: {prepare(value, indent)}\n'
        elif status == 'NESTED':
            result += f'{spacer}  {key}: {stylish(value, indent=indent + 4)}\n'
    else:
        result += f'{spacer[2:]}' + '}'
    result = result.replace('True', 'true').replace('False', 'false').\
        replace('None', 'null')
    return result


def prepare(value, indent):
    if isinstance(value, dict):
        return prepare_dict(value, indent)
    else:
        return value


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
