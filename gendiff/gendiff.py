import pathlib

from gendiff.cli import formatter
from gendiff.file_parser import get_data
from .tree import get_diff


def read_file(filepath: str) -> tuple:
    file = pathlib.Path(filepath)
    extension = file.suffix
    return file, extension


def generate_diff(path_file1, path_file2, style='stylish'):
    file1, extension1 = read_file(path_file1)
    file2, extension2 = read_file(path_file2)
    data1 = get_data(file1, extension1)
    data2 = get_data(file2, extension2)
    diff = get_diff(data1, data2)
    return formatter(diff, style)
