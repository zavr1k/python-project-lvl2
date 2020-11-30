from gendiff.gendiff import generate_diff
from gendiff.file_parser import get_path


def test_flat_json() -> None:
    reality = generate_diff(get_path('tests/fixtures/first.json'),
                            get_path('tests/fixtures/second.json'))
    expectation = get_path('tests/fixtures/result.txt').read_text()
    assert reality == expectation


def test_flat_yml() -> None:
    reality = generate_diff(get_path('tests/fixtures/first.yml'),
                            get_path('tests/fixtures/second.yml'))
    expectation = get_path('tests/fixtures/result.txt').read_text()
    assert reality == expectation
