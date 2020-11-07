from gendiff.formaters import stylish, plain, json_formating
from gendiff.generate_diff import gen_diff


def open_and_read(path):
    with open(path) as result_file:
        return result_file.read()


def test_simple_json_files():
    result = open_and_read("./tests/fixtures/simple_json_result.txt")
    output = gen_diff("./tests/fixtures/file1.json", "./tests/fixtures/file2.json", formater=lambda x:stylish.stylish(x,sorting=True))
    assert output == result


def test_simple_yaml_files():
    result = open_and_read("./tests/fixtures/simple_yaml_result.txt")
    output = gen_diff("./tests/fixtures/file1.yaml", "./tests/fixtures/file2.yaml", formater=lambda x:stylish.stylish(x,sorting=True))
    assert output == result

def test_json_files_with_stylish():
    result = open_and_read("./tests/fixtures/stylish_result.txt")[:-1]
    output = gen_diff("./tests/fixtures/file1b.json", "./tests/fixtures/file2b.json", formater=lambda x:stylish.stylish(x,sorting=True))
    assert output == result


def test_yaml_files_with_stylish():
    result = open_and_read("./tests/fixtures/stylish_result.txt")[:-1]
    output = gen_diff("./tests/fixtures/file1b.yaml", "./tests/fixtures/file2b.yaml", formater=lambda x:stylish.stylish(x,sorting=True))
    assert output == result


def test_json_files_with_plain():
    result = open_and_read("./tests/fixtures/plain_result.txt")
    output = gen_diff("./tests/fixtures/file1b.json", "./tests/fixtures/file2b.json", formater=lambda x: plain.plain(x,sorting=True))
    assert output == result


def test_yaml_files_with_plain():
    result = open_and_read("./tests/fixtures/plain_result.txt")
    output = gen_diff("./tests/fixtures/file1b.yaml", "./tests/fixtures/file2b.yaml", formater=lambda x: plain.plain(x,sorting=True))
    assert output == result


def test_json_files_with_json():
    result = open_and_read("./tests/fixtures/json_result.txt")
    output = gen_diff("./tests/fixtures/file1b.json", "./tests/fixtures/file2b.json", formater=lambda x: json_formating.json(x,sorting=True))
    assert output == result


def test_yaml_files_with_json():
    result = open_and_read("./tests/fixtures/json_result.txt")
    output = gen_diff("./tests/fixtures/file1b.yaml", "./tests/fixtures/file2b.yaml", formater=lambda x: json_formating.json(x,sorting=True))
    assert output == result