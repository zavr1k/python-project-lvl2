import json


def generate_diff(path_file1, path_file2):
    first_file = json.load(open(path_file1))
    second_file = json.load(open(path_file2))

    #  Prepare keys
    first_keys = first_file.keys()
    second_keys = second_file.keys()
    added_pos = second_keys - first_keys
    removed_pos = first_keys - second_keys
    all_keys = sorted(first_keys | second_keys)

    #  Fill the difference
    diff = []
    for key in all_keys:
        if key in added_pos:
            diff.append({
                'status': '+',
                'key': key,
                'value': second_file[key]
            })
        elif key in removed_pos:
            diff.append({
                'status': '-',
                'key': key,
                'value': first_file[key]
            })
        elif first_file[key] == second_file[key]:
            diff.append({
                'status': ' ',
                'key': key,
                'value': first_file[key]
            })
        else:
            diff.append({
                'status': '-',
                'key': key,
                'value': first_file[key]
            })
            diff.append({
                'status': '+',
                'key': key,
                'value': second_file[key]
            })

    #  Collecting the string
    result = '{\n'
    for d in diff:
        result += f' {d["status"]} {d["key"]}: {d["value"]}\n'
    result += '}'
    result = result.replace('True', 'true').replace('False', 'false')
    return result
