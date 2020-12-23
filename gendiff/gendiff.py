from gendiff.file_parser import get_data
from gendiff.cli import formatter
from .compare import get_diff


def generate_diff(path_file1, path_file2, style='stylish'):
    data1 = get_data(path_file1)
    data2 = get_data(path_file2)
    diff = get_diff(data1, data2)
    return formatter(diff, style)
