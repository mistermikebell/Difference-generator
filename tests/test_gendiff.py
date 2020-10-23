

""" Generate difference test """

from gendiff.generate_diff import gen_diff


def test_files_diff():
    result = open("./tests/fixtures/result.txt").read()[:-1]
    output = gen_diff("./tests/fixtures/file1.json", "./tests/fixtures/file2.json")
    assert output == result
