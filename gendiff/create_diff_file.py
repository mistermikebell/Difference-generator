

import json


def get_value(items, key):
    return items.get(key)


def get_keys(items):
    return set(items.keys())


def get_format_line(items, key):
    return "{}: {}".format(key, get_value(items, key))


def get_difference(compare_file, target_file):
    keys_compare = get_keys(compare_file)
    keys_target = get_keys(target_file)
    diff_keys = keys_target - keys_compare
    diff_items = list(map(
        lambda key: get_format_line(target_file, key),
        diff_keys)
    )
    return sorted(diff_items)


def get_intersec(left_file, right_file):
    keys_left = get_keys(left_file)
    keys_right = get_keys(right_file)
    intersec = keys_right & keys_left
    return sorted(list(intersec))


def is_values_simillar(left_file, right_file, key):
    val_left = get_value(left_file, key)
    val_right = get_value(right_file, key)
    if val_left == val_right:
        return True
    return False


def make_output(right_diff, left_diff, adjusted_intersec):
    output = ""
    output += "{\n"
    for line in left_diff:
        output += " - {}\n".format(line)
    for line in right_diff:
        output += " + {}\n".format(line)
    for line in adjusted_intersec:
        output += line + "\n"
    output += "}"
    return output


def generate_diff(left_file_path, right_file_path):
    left_file = json.load(open(left_file_path))
    right_file = json.load(open(right_file_path))
    right_diff = get_difference(left_file, right_file)
    left_diff = get_difference(right_file, left_file)
    intersec = get_intersec(left_file, right_file)
    adjusted_intersec = []
    for key in intersec:
        if is_values_simillar(left_file, right_file, key):
            adjusted_intersec.append('   ' + get_format_line(right_file, key))
        else:
            adjusted_intersec.append(' + ' + get_format_line(right_file, key))
            adjusted_intersec.append(' - ' + get_format_line(left_file, key))
    output = make_output(right_diff,
                         left_diff,
                         adjusted_intersec)
    return output