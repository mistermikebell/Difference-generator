import json as js

import pytest

from gendiff.generate_diff import generate_diff


def open_and_read(file_path):
    with open(file_path) as result_file:
        return result_file.read()


@pytest.mark.parametrize('format', ['json', 'yaml'])
def test(format):
    path_1 = f"./tests/fixtures/file1.{format}"
    path_2 = f"./tests/fixtures/file2.{format}"
    expected_stylish = open_and_read('./tests/fixtures/stylish.txt')
    expeсted_plain = open_and_read('./tests/fixtures/plain.txt')
    expeсted_json = js.loads(open_and_read("./tests/fixtures/json.txt"))
    assert expected_stylish == generate_diff(path_1, path_2)
    assert expeсted_plain == generate_diff(path_1, path_2, 'plain')
    assert expeсted_json == js.loads(generate_diff(path_1, path_2, 'json'))

path_1 = "../tests/fixtures/file1.json"
path_2 = "../tests/fixtures/file2.json"
print(generate_diff(path_1, path_2, 'plain'))