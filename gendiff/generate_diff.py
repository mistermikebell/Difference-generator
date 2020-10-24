
from gendiff.file_loader import load_file

from gendiff.dict_commands import get_value, get_keys


LEFT_FILE_NEW_ITEM_STATUS = 'left difference'
RIGHT_FILE_NEW_ITEM_STATUS = 'right difference'
ITEM_NO_CHANGE_STATUS = 'no change'
ITEM_CHANGE_STATUS = 'changed'
CHANGE_SIGNS = {'left difference': '-',
                'right difference': '+',
                'no change': ' '}


def compile_diff_info(items, key, status):
    return key, {'status': status,
                 'value': get_value(items, key)}


def get_difference(compare_file, target_file, status):
    keys_compare = get_keys(compare_file)
    keys_target = get_keys(target_file)
    diff_keys = keys_target - keys_compare
    diff_items = dict(map(
        lambda key: compile_diff_info(target_file, key, status),
        diff_keys)
    )
    return dict(sorted(diff_items.items()))


def is_values_simillar(left_file, right_file, key):
    val_left = get_value(left_file, key)
    val_right = get_value(right_file, key)
    if val_left == val_right:
        return True
    return False


def get_intersec(left_file, right_file):
    keys_left = get_keys(left_file)
    keys_right = get_keys(right_file)
    intersec = keys_right & keys_left
    adjusted_intersec = dict()
    for key in intersec:
        if is_values_simillar(left_file, right_file, key):
            adjusted_intersec.update(
                dict([compile_diff_info(right_file,
                                        key,
                                        ITEM_NO_CHANGE_STATUS)]
                     )
            )
        else:
            adjusted_intersec[key] = {
                'status': ITEM_CHANGE_STATUS,
                'values': {
                    'value_1':
                        dict([compile_diff_info(left_file,
                                                key,
                                                LEFT_FILE_NEW_ITEM_STATUS)]),
                    'value_2':
                        dict([compile_diff_info(right_file,
                                                key,
                                                RIGHT_FILE_NEW_ITEM_STATUS)])
                }
            }
    return dict(sorted(adjusted_intersec.items()))


def make_output_str(diff, output):
    for key, info in diff.items():
        if info['status'] == 'changed':
            for item in info['values'].values():
                output = make_output_str(item, output)
        else:
            status = get_value(info, 'status')
            sign = CHANGE_SIGNS.get(status)
            value = get_value(info, 'value')
            output += ' {} {}: {}\n'.format(sign, key, value)
    return output


def gen_diff(left_file_path, right_file_path):
    left_file = load_file(left_file_path)
    right_file = load_file(right_file_path)
    right_diff = get_difference(left_file,
                                right_file,
                                RIGHT_FILE_NEW_ITEM_STATUS)
    left_diff = get_difference(right_file,
                               left_file,
                               LEFT_FILE_NEW_ITEM_STATUS)
    intersec = get_intersec(left_file, right_file)
    diff = {**left_diff, **right_diff, **intersec}
    output_string = make_output_str(diff, "")
    return '{\n' + output_string + '}'
