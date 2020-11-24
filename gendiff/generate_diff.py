from gendiff.file_loader import load_file
from gendiff.diff_structure import compile

def gen_diff(before_file_path, after_file_path, formater):
    before_file = load_file(before_file_path)
    after_file = load_file(after_file_path)
    diff = compile(before_file, after_file)
    return formater(diff)
