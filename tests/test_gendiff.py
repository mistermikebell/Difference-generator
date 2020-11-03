

""" Generate difference test """
from gendiff.formaters.stylish import stylish

from gendiff.formaters.plain import plain

from gendiff.formaters.json_formating import json

from gendiff.generate_diff import gen_diff


def test_simple_json_files():
    result = open("./tests/fixtures/simple_json_result.txt").read()
    output = gen_diff("./tests/fixtures/file1.json", "./tests/fixtures/file2.json", formater=stylish)
    assert output == result


def test_simple_yaml_files():
    result = open("./tests/fixtures/simple_yaml_result.txt").read()
    output = gen_diff("./tests/fixtures/file1.yaml", "./tests/fixtures/file2.yaml", formater=stylish)
    assert output == result

def test_json_files_with_stylish():
    result = open("./tests/fixtures/stylish_result.txt").read()[:-1]
    output = gen_diff("./tests/fixtures/file1b.json", "./tests/fixtures/file2b.json", formater=stylish)
    assert output == result


def test_yaml_files_with_stylish():
    result = open("./tests/fixtures/stylish_result.txt").read()[:-1]
    output = gen_diff("./tests/fixtures/file1b.yaml", "./tests/fixtures/file2b.yaml", formater=stylish)
    assert output == result


def test_json_files_with_plain():
    result = open("./tests/fixtures/plain_result.txt").read()
    output = gen_diff("./tests/fixtures/file1b.json", "./tests/fixtures/file2b.json", formater=plain)
    assert output == result


def test_yaml_files_with_plain():
    result = open("./tests/fixtures/plain_result.txt").read()
    output = gen_diff("./tests/fixtures/file1b.yaml", "./tests/fixtures/file2b.yaml", formater=plain)
    assert output == result


def test_json_files_with_json():
    result = open("./tests/fixtures/json_result.txt").read()
    output = gen_diff("./tests/fixtures/file1b.json", "./tests/fixtures/file2b.json", formater=json)
    assert output == result


def test_yaml_files_with_json():
    result = open("./tests/fixtures/json_result.txt").read()
    output = gen_diff("./tests/fixtures/file1b.yaml", "./tests/fixtures/file2b.yaml", formater=json)
    assert output == result
