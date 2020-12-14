from gendiff.file_parser import get_data
from gendiff.statuses import ADDED, REMOVED, CHANGED, NO_CHANGED, NESTED
from gendiff.format.stylish import stylish


def generate_diff(path_file1, path_file2, style='stylish'):
    data1 = get_data(path_file1)
    data2 = get_data(path_file2)
    diff = get_diff(data1, data2)
    if style == 'stylish':
        return stylish(diff)


def get_diff(data1: dict, data2: dict) -> dict:
    diff = {}
    for key in data1.keys() - data2.keys():
        diff[key] = (REMOVED, data1.get(key))
    for key in data2.keys() - data1.keys():
        diff[key] = (ADDED, data2.get(key))
    for key in data1.keys() & data2.keys():
        if isinstance(data1[key], dict) and isinstance(data2[key], dict):
            if data1[key] == data2[key]:
                diff[key] = (NO_CHANGED, data2[key])
            else:
                diff[key] = (NESTED, get_diff(data1[key], data2[key]))
        else:
            if data1[key] == data2[key]:
                diff[key] = (NO_CHANGED, data2[key])
            else:
                diff[key] = (CHANGED, (data1[key], data2[key]))
    return diff
