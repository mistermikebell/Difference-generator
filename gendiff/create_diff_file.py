

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
    return diff_items


def get_intersec(left_file, right_file):
    keys_left = get_keys(left_file)
    keys_right = get_keys(right_file)
    intersec = keys_right & keys_left
    return intersec


def is_values_simillar(left_file, right_file, key):
    val_left = get_value(left_file, key)
    val_right = get_value(right_file, key)
    if val_left == val_right:
        return True
    return False


def make_compare_file(right_diff, left_diff, adjusted_intersec):
    output_file_name = "left_file_right_file.txt"
    with open(output_file_name, 'a') as output_file:
        output_file.write("{\n")
        for line in left_diff:
            output_file.write(" - {}\n".format(line))
        for line in right_diff:
            output_file.write(" + {}\n".format(line))
        for line in adjusted_intersec:
            output_file.write(line + "\n")
        output_file.write("}")
    return output_file_name


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
    output_file_name = make_compare_file(right_diff,
                                         left_diff,
                                         adjusted_intersec)
    with open(output_file_name, 'r') as output:
        return output.read()
