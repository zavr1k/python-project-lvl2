from gendiff.gendiff import generate_diff
from gendiff.file_parser import get_path
import pytest


testdata = [
    (get_path('tests/fixtures/first.json'),
     get_path('tests/fixtures/second.json'),
     get_path('tests/fixtures/result.txt').read_text()),
    (get_path('tests/fixtures/first.yml'),
     get_path('tests/fixtures/second.yml'),
     get_path('tests/fixtures/result.txt').read_text()),
    (get_path('tests/fixtures/first_complex.json'),
     get_path('tests/fixtures/second_complex.json'),
     get_path('tests/fixtures/complex_result.txt').read_text()),
    (get_path('tests/fixtures/first_complex.yml'),
     get_path('tests/fixtures/second_complex.yml'),
     get_path('tests/fixtures/complex_result.txt').read_text()),
]


@pytest.mark.parametrize("a,b,expected", testdata)
def test_diff(a, b, expected):
    diff = generate_diff(a, b)
    assert diff == expected
