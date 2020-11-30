from gendiff.diff_tree import REMOVED, ADDED, CHANGED, NESTED

ADDED_MESSAGE = "Property '{}{}' was added with value: {}"
REMOVED_MESSAGE = "Property '{}{}' was removed"
CHANGED_MESSAGE = "Property '{}{}' was updated. From {} to {}"
COMPLEX_VALUE = "[complex value]"


def stringify(item):
    if isinstance(item, bool):
        return str(item).lower()
    if item is None:
        return "null"
    if isinstance(item, dict):
        return COMPLEX_VALUE
    return "'{}'".format(item)


def plain(diff):
    output = []

    def iter(tree, path):
        for key in tree.keys():
            status, value = tree[key]
            if status == NESTED:
                iter(value, path + key + '.')
                path = ''
            if status == ADDED:
                output.append(ADDED_MESSAGE.format(path,
                                                   key,
                                                   stringify(value)))
            if status == REMOVED:
                output.append(REMOVED_MESSAGE.format(path, key))
            if status == CHANGED:
                output.append(CHANGED_MESSAGE.format(path, key,
                                                     stringify(value[0]),
                                                     stringify(value[1])))
    iter(diff, '')
    return '\n'.join(output)
