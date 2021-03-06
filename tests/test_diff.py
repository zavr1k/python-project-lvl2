from pathlib import Path

import pytest
import json
import tempfile

from gendiff import generate_diff


def path_to(file_name: str):
    based_path = Path(__file__).parent.joinpath('fixtures')
    full_path = based_path.joinpath(file_name)
    return full_path


def read_file(file_name: str):
    path_file = path_to(file_name)
    with open(path_file) as file:
        return file.read()


test_cases = [
    (path_to('file1.json'),
     path_to('file2.json'),
     'stylish',
     read_file('result_stylish.txt')),
    (path_to('file1.yml'),
     path_to('file2.yml'),
     'stylish',
     read_file('result_stylish.txt')),
    (path_to('file1.yml'),
     path_to('file2.yml'),
     'plain',
     read_file('result_plain.txt')),
    (path_to('file1.json'),
     path_to('file2.json'),
     'plain',
     read_file('result_plain.txt')),
    (path_to('file1.json'),
     path_to('file2.yml'),
     'stylish',
     read_file('result_stylish.txt'))
]


@pytest.mark.parametrize("file1, file2, output_format, expected", test_cases)
def test_diff(file1, file2, output_format, expected):
    diff = generate_diff(file1, file2, output_format)
    assert diff == expected


def test_json_formatter():
    diff = generate_diff(path_to('file1.json'), path_to('file2.json'), 'json')
    json1 = json.loads(diff)
    json2 = json.loads(read_file('result_json.json'))
    assert json1 == json2


def test_with_unsupported_file_format():
    wrong_file = tempfile.NamedTemporaryFile(suffix='.txt')
    with pytest.raises(ValueError):
        generate_diff(path_to(wrong_file.name), path_to('file1.json'))
