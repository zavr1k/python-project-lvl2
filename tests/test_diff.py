from pathlib import Path

import pytest

from gendiff.gendiff import generate_diff


def path_to(file_name: str):
    based_path = Path().cwd().joinpath('tests/fixtures')
    full_path = based_path.joinpath(file_name)
    return full_path


def read_file(file_name: str):
    file = path_to(file_name)
    return file.read_text()


test_cases = [
    (path_to('file1.json'),  # tests with two json files format - stylish
     path_to('file2.json'),
     'stylish',
     read_file('result_stylish.txt')),
    (path_to('file1.yml'),  # tests with two yml files format - stylish
     path_to('file2.yml'),
     'stylish',
     read_file('result_stylish.txt')),
    (path_to('file1.yml'),  # tests with two yml files format - plain
     path_to('file2.yml'),
     'plain',
     read_file('result_plain.txt')),
    (path_to('file1.json'),  # tests with two json files format - plain
     path_to('file2.json'),
     'plain',
     read_file('result_plain.txt')),
    (path_to('file1.json'),  # tests with different file formats
     path_to('file2.yml'),
     'stylish',
     read_file('result_stylish.txt')),
]


@pytest.mark.parametrize("file1, file2, output_format, expected", test_cases)
def test_diff(file1, file2, output_format, expected):
    diff = generate_diff(file1, file2, output_format)
    assert diff == expected
