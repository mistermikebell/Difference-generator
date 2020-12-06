from gendiff.formaters import format
from gendiff.loader import get_file_data
from gendiff import diff_tree


def generate_diff(before_file_path, after_file_path, formater='stylish'):
    before_file = get_file_data(before_file_path)
    after_file = get_file_data(after_file_path)
    diff = diff_tree.build(before_file, after_file)
    transform_to_format = format.choose(formater)
    return transform_to_format(diff)
