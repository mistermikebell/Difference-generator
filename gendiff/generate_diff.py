from gendiff.file_loader import load_file

from gendiff.statuses import NO_CHANGE_STATUS, CHANGED_STATUS, INNER_CHANGE, ADDED_STATUS, DELETED_STATUS
from gendiff.formaters.plain import plain
from gendiff.formaters.json_formating import json


def compile_info(key, value, status):
    if status != NO_CHANGE_STATUS and isinstance(value, dict):
        return (key, {'status': status, 'value': dict(map(lambda k: compile_info(k, value[k], 'nothing changed'), value.keys()))})
    elif status == CHANGED_STATUS:
        value = [dict(map(lambda k: compile_info(k, v[k], INNER_CHANGE), v.keys())) if isinstance(v, dict) else v for v in value]
        value = [{'status': DELETED_STATUS, 'value': value[0]}, {'status': ADDED_STATUS, 'value': value[1]}]
    return (key, {'status': status, 'value': value})


def make_diff(before_dict, after_dict):
    added_keys = sorted(list(after_dict.keys() - before_dict.keys()))
    added_items = dict(map(lambda key: compile_info(key, after_dict[key], ADDED_STATUS), added_keys))
    deleted_keys = sorted(list(before_dict.keys() - after_dict.keys()))
    deleted_items = dict(map(lambda key: compile_info(key, before_dict[key], DELETED_STATUS), deleted_keys))
    intersec = sorted(list(before_dict.keys() & after_dict.keys()))
    adjusted_intersec = {}
    for key in intersec:
        if isinstance(before_dict[key], dict) and isinstance(after_dict[key], dict):
            adjusted_value = make_diff(before_dict[key], after_dict[key])
            adjusted_intersec.update(dict([compile_info(key, adjusted_value, NO_CHANGE_STATUS)]))
        elif before_dict[key] == after_dict[key]:
            adjusted_intersec.update(dict([compile_info(key, before_dict[key], NO_CHANGE_STATUS)]))
        else:
            adjusted_intersec.update(dict([compile_info(key, [before_dict[key], after_dict[key]], CHANGED_STATUS)]))
    return {**added_items, **deleted_items, **adjusted_intersec}


def gen_diff(before_file_path, after_file_path, format):
    before_file = load_file(before_file_path)
    after_file = load_file(after_file_path)
    diff = make_diff(before_file, after_file)
    return format(diff)

print(gen_diff('../tests/fixtures/file1b.yaml', '../tests/fixtures/file2b.yaml', json))