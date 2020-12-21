from gendiff.file_parser import get_data
from gendiff.format.json import to_json
from gendiff.format.plain import to_plain
from gendiff.format.stylish import stylish
from .diff import get_diff


def generate_diff(path_file1, path_file2, style='stylish'):
    data1 = get_data(path_file1)
    data2 = get_data(path_file2)
    diff = get_diff(data1, data2)
    if style == 'stylish':
        return stylish(diff)
    if style == 'plain':
        return to_plain(diff)
    if style == 'json':
        return to_json(diff)
