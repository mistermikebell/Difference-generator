import json as js

import pytest

from gendiff import generate_diff


def open_and_read(file_path):
    with open(file_path) as result_file:
        return result_file.read()


@pytest.mark.parametrize('format', ['json', 'yaml'])
def test_generate_diff(format):
    path_1 = f"./tests/fixtures/file1.{format}"
    path_2 = f"./tests/fixtures/file2.{format}"
    expected_stylish = open_and_read('./tests/fixtures/stylish.txt')
    expected_plain = open_and_read('./tests/fixtures/plain.txt')
    expected_json = js.loads(open_and_read("./tests/fixtures/json.txt"))
    assert expected_stylish == generate_diff(path_1, path_2)
    assert expected_plain == generate_diff(path_1, path_2, 'plain')
    assert expected_json == js.loads(generate_diff(path_1, path_2, 'json'))
