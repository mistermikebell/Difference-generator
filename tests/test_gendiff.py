import json

from gendiff.formaters import json_formating, plain, stylish
from gendiff.diff_generator import gen_diff


def open_and_read(file_path):
    with open(file_path) as result_file:
        return result_file.read()


def test_simple_stylish():
    path_1 = './tests/fixtures/simple_file1.json'
    path_2 = './tests/fixtures/simple_file2.json'
    expected = open_and_read("./tests/fixtures/simple_stylish.txt")
    assert expected == gen_diff(path_1, path_2, stylish.stylish)


def test():
    path_1 = './tests/fixtures/file1.json'
    path_2 = './tests/fixtures/file2.json'
    expected_stylish = open_and_read('./tests/fixtures/stylish.txt')
    expeсted_plain = open_and_read('./tests/fixtures/plain.txt')
    expeсted_json = json.loads(open_and_read("./tests/fixtures/json.txt"))
    assert expected_stylish == gen_diff(path_1, path_2, stylish.stylish)
    assert expeсted_plain == gen_diff(path_1, path_2, plain.plain)
    assert expeсted_json == json.loads(gen_diff(path_1,
                                                path_2,
                                                json_formating.json))
