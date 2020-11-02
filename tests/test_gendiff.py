

""" Generate difference test """
from gendiff.formaters.stylish import stylish
from gendiff.generate_diff import gen_diff


def test_simple_json_files():
    result = open("./tests/fixtures/simple_json_result.txt").read()[:-1]
    output = gen_diff("./tests/fixtures/file1.json", "./tests/fixtures/file2.json", format=stylish)
    assert output == result


def test_simple_yaml_files():
    result = open("./tests/fixtures/simple_yaml_result.txt").read()[:-1]
    output = gen_diff("./tests/fixtures/file1.yaml", "./tests/fixtures/file2.yaml", format=stylish)
    assert output == result

def test_json_files_with_stylish():
    result = open("./tests/fixtures/result.txt").read()[:-1]
    output = gen_diff("./tests/fixtures/file1b.json", "./tests/fixtures/file2b.json", format=stylish)
    assert output == result


def test_yaml_files_with_stylish():
    result = open("./tests/fixtures/result.txt").read()[:-1]
    output = gen_diff("./tests/fixtures/file1b.yaml", "./tests/fixtures/file2b.yaml", format=stylish)
    assert output == result