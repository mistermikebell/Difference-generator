

""" Generate difference test """

from gendiff.create_diff_file import generate_diff


def test_files_diff():
    result = open("./tests/fixtures/result.txt").read()
    output = generate_diff("./tests/fixtures/file1.json", "./tests/fixtures/file2.json")
    print("This is output:", output)
    print("Result:", result)
    assert output == result

test_files_diff()
