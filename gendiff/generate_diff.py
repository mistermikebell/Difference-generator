from gendiff.loader import get_file_data
from gendiff.diff_tree import build
from gendiff.formaters import format


def generate_diff(before_file_path, after_file_path, formater='stylish'):
    before_dict = get_file_data(before_file_path)
    after_dict = get_file_data(after_file_path)
    diff = build(before_dict, after_dict)
    used_formater = format.choose(formater)
    return used_formater(diff)
