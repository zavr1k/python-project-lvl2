from gendiff.statuses import ADDED, CHANGED, NO_CHANGED, REMOVED, NESTED


def stylish(diff: dict, indent=2) -> str:
    spacer = ' ' * indent
    result = '{\n'
    for key, (status, value) in sorted(diff.items()):
        if status == ADDED:
            result += f'{spacer}+ {key}: {prepare(value, indent)}\n'
        elif status == REMOVED:
            result += f'{spacer}- {key}: {prepare(value, indent)}\n'
        elif status == CHANGED:
            result += f'{spacer}- {key}: {prepare(value[0], indent)}\n'
            result += f'{spacer}+ {key}: {prepare(value[1], indent)}\n'
        elif status == NO_CHANGED:
            result += f'{spacer}  {key}: {prepare(value, indent)}\n'
        elif status == NESTED:
            result += f'{spacer}  {key}: {stylish(value, indent=indent + 4)}\n'
    else:
        result += f'{spacer[2:]}' + '}'
    result = result.replace('True', 'true').replace('False', 'false').\
        replace('None', 'null')
    return result


def prepare(value, indent):
    if not isinstance(value, dict):
        return value
    spacer = ' ' * (indent + 6)
    result = '{\n'
    for key, value in value.items():
        if isinstance(value, dict):
            result += f'{spacer}{key}: {prepare(value, indent+4)}\n'
        else:
            result += f'{spacer}{key}: {value}\n'
    else:
        result += f'{spacer[4:]}' + '}'
    return result


# a = {'common': ('nested',
#             {'follow': ('added', False),
#              'setting1': ('no_changed', 'Value 1'),
#              'setting2': ('removed', 200),
#              'setting3': ('changed', (True, None)),
#              'setting4': ('added', 'blah blah'),
#              'setting5': ('added', {'key5': 'value5'}),
#              'setting6': ('nested',
#                           {'doge': ('nested',
#                                     {'wow': ('changed', ('', 'so much'))}),
#                            'key': ('no_changed', 'value'),
#                            'ops': ('added', 'vops')})}),
#     'group1': ('nested',
#             {'baz': ('changed', ('bas', 'bars')),
#              'foo': ('no_changed', 'bar'),
#              'nest': ('changed', ({'key': 'value'}, 'str'))}),
#     'group2': ('removed', {'abc': 12345, 'deep': {'id': 45}}),
#     'group3': ('added', {'deep': {'id': {'number': 45}}, 'fee': 100500})}
#
# print(stylish(a))
