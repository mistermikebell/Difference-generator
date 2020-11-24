import pytest

from gendiff.formaters import json_formating, plain, stylish
from gendiff.file_loader import load_file
from gendiff.generate_diff import gen_diff


def open_and_read(file_path):
    with open(file_path) as result_file:
        return result_file.read()


def test_simple_json_files():
    result = open_and_read("./tests/fixtures/simple_json_result.txt")
    output = gen_diff("./tests/fixtures/file1.json",
                      "./tests/fixtures/file2.json",
                      stylish.stylish)
    assert output == result


def test_simple_yaml_files():
    result = open_and_read("./tests/fixtures/simple_yaml_result.txt")
    output = gen_diff("./tests/fixtures/file1.yaml",
                      "./tests/fixtures/file2.yaml",
                      stylish.stylish)
    assert output == result


@pytest.mark.parametrize(gen_diff("./tests/fixtures/file1b.json",
                                  "./tests/fixtures/file2b.json",
                                  stylish.stylish))
@pytest.mark.parametrize(gen_diff("./tests/fixtures/file1b.yaml",
                                  "./tests/fixtures/file2b.yaml",
                                  stylish.stylish))
def test_stylish(output):
    assert output == open_and_read("./tests/fixtures/stylish_result.txt")


@pytest.mark.parametrize(gen_diff("./tests/fixtures/file1b.json",
                                  "./tests/fixtures/file2b.json",
                                  plain.plain))
@pytest.mark.parametrize(gen_diff("./tests/fixtures/file1b.yaml",
                         "./tests/fixtures/file2b.yaml",
                         plain.plain))
def test_plain(output):
    assert output == open_and_read("./tests/fixtures/plain_result.txt")


@pytest.mark.parametrize(gen_diff("./tests/fixtures/file1b.json",
                                 "./tests/fixtures/file2b.json",
                                 json_formating.json))
@pytest.mark.parametrize(gen_diff("./tests/fixtures/file1b.yaml",
                                  "./tests/fixtures/file2b.yaml",
                                  json_formating.json))
def test_json_files_with_json(output):
    assert output == load_file("./tests/fixtures/json_result.json")
