from gendiff.tree import ADDED, REMOVED, CHANGED, UNCHANGED, NESTED


def prepare_value(value, indent):
    if isinstance(value, dict):
        return prepare_dict(value, indent)
    elif isinstance(value, bool):
        return str(value).lower()
    else:
        return str(value).replace('None', 'null')


def prepare_dict(value, indent):
    spacer = ' ' * (indent + 6)
    strings = ['{']
    strings.extend(prepare_strings(value, indent))
    strings.append(f'{spacer[4:]}{chr(125)}')
    return '\n'.join(strings)


def prepare_strings(value, indent):
    spacer = ' ' * (indent + 6)
    strings = []
    for key, value in value.items():
        if isinstance(value, dict):
            strings.append(f'{spacer}{key}: {chr(123)}')
            strings.extend(prepare_strings(value, indent + 4))
            strings.append(f'{spacer}{chr(125)}')
        else:
            strings.append(f'{spacer}{key}: {value}')
    return strings


def prepares_changes(tree: dict, indent=2) -> list:
    strings = []
    spacer = ' ' * indent

    for node in tree['children']:
        if node['type'] == ADDED:
            strings.append(f'{spacer}+ {node["key"]}: '
                           f'{prepare_value(node["value"], indent)}')
        elif node['type'] == REMOVED:
            strings.append(f'{spacer}- {node["key"]}: '
                           f'{prepare_value(node["value"], indent)}')
        elif node['type'] == CHANGED:
            strings.append(f'{spacer}- {node["key"]}: '
                           f'{prepare_value(node["old_value"], indent)}')
            strings.append(f'{spacer}+ {node["key"]}: '
                           f'{prepare_value(node["new_value"], indent)}')
        elif node['type'] == UNCHANGED:
            strings.append(f'{spacer}  {node["key"]}: '
                           f'{prepare_value(node["value"], indent)}')
        elif node['type'] == NESTED:
            strings.append(f'{spacer}  {node["key"]}: {chr(123)}')
            strings.extend(prepares_changes(node, indent=indent + 4))
            strings.append(f'{spacer}  {chr(125)}')

    return strings


def transform(diff: dict) -> str:
    changes = ['{']
    changes.extend(prepares_changes(diff))
    changes.append('}')
    return '\n'.join(changes)
