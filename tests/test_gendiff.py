

""" Generate difference test """

from gendiff.create_diff_file import generate_diff


def test_files_diff():
    result = open("result.txt").read()
    output = generate_diff("file1.json", "file2.json")
    print(output)
    print(result)
    assert output == result

test_files_diff()
