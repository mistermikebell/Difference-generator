from gendiff.loader import load_file
from gendiff.structure_builder import compile
from gendiff.parser import parse


def gen_diff(before_file_path, after_file_path, formater):
    before_content, before_extension = load_file(before_file_path)
    before_dict = parse(before_content, before_extension)
    after_content, after_extension = load_file(after_file_path)
    after_dict = parse(after_content, after_extension)
    if before_extension != after_extension:
        raise Exception('Extensions of files are different. '
                        'Please, specify files with one format')
    diff = compile(before_dict, after_dict)
    return formater(diff)
