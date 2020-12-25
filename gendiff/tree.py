ADDED, REMOVED, CHANGED, NO_CHANGED, NESTED, ROOT = \
    'added', 'removed', 'changed', 'no changed', 'nested', 'root'


def add_children(file1: dict, file2: dict) -> list:
    result = []
    for key in file2.keys() - file1.keys():
        result.append({
            'key': key,
            'type': ADDED,
            'value': file2[key]
        })

    for key in file1.keys() - file2.keys():
        result.append({
            'key': key,
            'type': REMOVED,
            'value': file1[key]
        })

    for key in file1.keys() & file2.keys():
        if file1[key] == file2[key]:
            result.append({
                'key': key,
                'type': NO_CHANGED,
                'value': file2[key]
            })
        elif (isinstance(file1[key], dict) and isinstance(file2[key], dict)) \
                and file1[key] != file2[key]:
            result.append({
                'key': key,
                'type': NESTED,
                'children': add_children(file1[key], file2[key])
            })
        elif not (isinstance(file1[key], dict)
                  and isinstance(file2[key], dict)) \
                and file1[key] != file2[key]:
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


# a ={
#   "common": {
#     "setting1": "Value 1",
#     "setting2": 200,
#     "setting3": True,
#     "setting6": {
#       "key": "value",
#       "doge": {
#         "wow": ""
#       }
#     }
#   },
#   "group1": {
#     "baz": "bas",
#     "foo": "bar",
#     "nest": {
#       "key": "value"
#     }
#   },
#   "group2": {
#     "abc": 12345,
#     "deep": {
#       "id": 45
#     }
#   }
# }
# b = {
#   "common": {
#     "follow": False,
#     "setting1": "Value 1",
#     "setting3": None,
#     "setting4": "blah blah",
#     "setting5": {
#       "key5": "value5"
#     },
#     "setting6": {
#       "key": "value",
#       "ops": "vops",
#       "doge": {
#         "wow": "so much"
#       }
#     }
#   },
#   "group1": {
#     "foo": "bar",
#     "baz": "bars",
#     "nest": "str"
#   },
#   "group3": {
#     "fee": 100500,
#     "deep": {
#       "id": {
#         "number": 45
#       }
#     }
#   }
# }
# from pprint import pprint
# pprint(get_diff(a, b))
