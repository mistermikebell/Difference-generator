from gendiff.file_loader import load_file

REMOVED = 'removed'
ADDED = 'added'
NO_CHANGED = 'no_changed'
CHANGED = 'changed'
NESTED = 'nested'


def make_diff(before_dict, after_dict):
    added_items = {key: (ADDED, after_dict[key])
                   for key in after_dict.keys() - before_dict.keys()}
    removed_items = {key: (REMOVED, before_dict[key])
                     for key in before_dict.keys() - after_dict.keys()}
    intersec = {}
    for key in before_dict.keys() & after_dict.keys():
        if isinstance(before_dict[key], dict) and isinstance(after_dict[key], dict):  # noqa: E501
            adjusted_value = make_diff(before_dict[key], after_dict[key])
            intersec[key] = (NESTED, adjusted_value)
        elif before_dict[key] == after_dict[key]:
            intersec[key] = (NO_CHANGED, before_dict[key])
        else:
            intersec[key] = (CHANGED, [before_dict[key], after_dict[key]])
    return {**added_items, **removed_items, **intersec}


def gen_diff(before_file_path, after_file_path, formater):
    before_file = load_file(before_file_path)
    after_file = load_file(after_file_path)
    diff = make_diff(before_file, after_file)
    return formater(diff)
