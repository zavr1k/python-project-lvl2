from gendiff.gendiff import generate_diff, get_path
from pathlib import Path


def test_flat_json() -> None:
    reality = generate_diff(get_path('tests/fixtures/first.json'),
                            get_path('tests/fixtures/second.json'))
    expectation = Path(get_path('tests/fixtures/result.txt')).read_text()
    assert reality == expectation


def test_flat_yml() -> None:
    reality = generate_diff(get_path('tests/fixtures/first.yml'),
                            get_path('tests/fixtures/second.yml'))
    expectation = get_path('tests/fixtures/result.txt').read_text()
    assert reality == expectation
