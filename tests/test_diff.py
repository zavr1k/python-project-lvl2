from gendiff.gendiff import generate_diff
from gendiff.file_parser import get_path
import pytest


test_data = [
    ('tests/fixtures/first.json',
     'tests/fixtures/second.json',
     'stylish',
     get_path('tests/fixtures/result.txt').read_text()),
    ('tests/fixtures/first.yml',
     'tests/fixtures/second.yml',
     'stylish',
     get_path('tests/fixtures/result.txt').read_text()),
    ('tests/fixtures/first_complex.json',
     'tests/fixtures/second_complex.json',
     'stylish',
     get_path('tests/fixtures/complex_result.txt').read_text()),
    ('tests/fixtures/first_complex.yml',
     'tests/fixtures/second_complex.yml',
     'stylish',
     get_path('tests/fixtures/complex_result.txt').read_text()),
    ('tests/fixtures/first_complex.json',
     'tests/fixtures/second_complex.json',
     'plain',
     get_path('tests/fixtures/plain_result.txt').read_text()),
]


@pytest.mark.parametrize("file1, file2, format_output, expected", test_data)
def test_diff(file1, file2, format_output, expected):
    diff = generate_diff(file1, file2, format_output)
    assert diff == expected
