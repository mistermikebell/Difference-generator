from gendiff.file_loader import load_file
from gendiff.constants import NO_CHANGE, CHANGED, ADDED, REMOVED


def make_diff(before_dict, after_dict):
    added_keys = after_dict.keys() - before_dict.keys()
    added_items = {key: (ADDED, after_dict[key]) for key in added_keys}
    removed_keys = before_dict.keys() - after_dict.keys()
    removed_items = {key: (REMOVED, before_dict[key]) for key in removed_keys}
    intersec = before_dict.keys() & after_dict.keys()
    adjusted_intersec = {}
    for key in intersec:
        if isinstance(before_dict[key], dict) \
          and isinstance(after_dict[key], dict):
            adjusted_value = make_diff(before_dict[key], after_dict[key])
            adjusted_intersec.update({key: (NO_CHANGE, adjusted_value)})
        elif before_dict[key] == after_dict[key]:
            adjusted_intersec.update({key: (NO_CHANGE, before_dict[key])})
        else:
            adjusted_intersec.update({key: (CHANGED, [before_dict[key], after_dict[key]])})
    return {**added_items, **removed_items, **adjusted_intersec}


def gen_diff(before_file_path, after_file_path, formater):
    before_file = load_file(before_file_path)
    after_file = load_file(after_file_path)
    diff = make_diff(before_file, after_file)
    return formater(diff)
