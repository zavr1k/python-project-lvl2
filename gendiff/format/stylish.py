from gendiff.tree import ADDED, REMOVED, CHANGED, UNCHANGED, NESTED


def prepare_value(value, indent):
    if isinstance(value, dict):
        return prepare_dict(value, indent)
    elif isinstance(value, bool):
        return str(value).lower()
    else:
        return str(value).replace('None', 'null')


def prepare_dict(value, indent):
    strings = []
    strings.extend(prepare_strings(value, indent))
    return '\n'.join(strings)


def prepare_strings(value, indent):
    spacer = ' ' * (indent + 6)
    strings = ['{']
    for key, value in value.items():
        if isinstance(value, dict):
            strings.append(f'{spacer}{key}: {{')
            strings.extend(prepare_strings(value, indent + 4)[1:])
        else:
            strings.append(f'{spacer}{key}: {value}')
    strings.append(f'{spacer[4:]}}}')
    return strings


def prepares_changes(tree: dict, indent=2) -> list:
    strings = ['{']
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
            strings.append(f'{spacer}  {node["key"]}: {{')
            strings.extend(prepares_changes(node, indent=indent + 4)[1:])
    strings.append(f'{spacer[2:]}}}')
    return strings


def format_stylish(diff: dict) -> str:
    changes = []
    changes.extend(prepares_changes(diff))
    return '\n'.join(changes)
