

""" Generate difference test """

from gendiff.generate_diff import gen_diff


def test_json_files():
    result = open("fixtures/json_result.txt").read()[:-1]
    output = gen_diff("./tests/fixtures/file1.json", "./tests/fixtures/file2.json")
    assert output == result

def test_yaml_files():
    result = open("fixtures/yaml_result.txt").read()[:-1]
    output = gen_diff("./tests/fixtures/file1.yaml", "./tests/fixtures/file2.yaml")
    assert output == result
