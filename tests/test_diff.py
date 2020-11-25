from gendiff.gendiff import generate_diff


def test_flat_json():
    result = generate_diff('./tests/fixtures/first.json',
                           './tests/fixtures/second.json')
    answer = open('./tests/fixtures/result.txt').read()
    assert result == answer
