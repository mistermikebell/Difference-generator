from gendiff.generate_diff import REMOVED, ADDED, CHANGED, NESTED

ADDED_MESSAGE = "Property '{}{}' was added with value: {}"
REMOVED_MESSAGE = "Property '{}{}' was removed"
CHANGED_MESSAGE = "Property '{}{}' was updated. From {} to {}"


def stringify(item):
    if not isinstance(item, list):
        item = [item]
    return ['[complex value]'
            if isinstance(val, dict) else "'{}'".format(val)
            for val in item]


def plain(diff):
    output = []

    def iter(tree, path):
        for key in sorted(tree.keys()):
            status, value = tree[key]
            if status == NESTED:
                iter(value, path + key + '.')
                path = ''
            converted_value = stringify(value)
            if status == ADDED:
                output.append(ADDED_MESSAGE.format(path,
                                                   key,
                                                   converted_value[0]))
            if status == REMOVED:
                output.append(REMOVED_MESSAGE.format(path, key))
            if status == CHANGED:
                output.append(CHANGED_MESSAGE.format(path, key,
                                                     converted_value[0],
                                                     converted_value[1]))
    iter(diff, '')
    return '\n'.join(output)
