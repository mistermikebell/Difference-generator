REMOVED = 'removed'
ADDED = 'added'
NO_CHANGED = 'no_changed'
CHANGED = 'changed'
NESTED = 'nested'
SIGNS = {REMOVED: '-',
         ADDED: '+',
         CHANGED: ' ',
         NESTED: ' '}
ADDED_MESSAGE = "Property '{}{}' was added with value: {}"
REMOVED_MESSAGE = "Property '{}{}' was removed"
CHANGED_MESSAGE = "Property '{}{}' was updated. From {} to {}"


def plain(diff):
    output = []
    def iter_str(tree, path):
        for key in sorted(tree.keys()):
            status, value = tree[key]
            if status == NESTED and isinstance(value, dict):
                iter_str(value, path + key + '.')
                path = ''
            if not isinstance(value, list):
                value = [value]
            adjusted_value = ['[complex value]'
                              if isinstance(val, dict)
                              else "'{}'".format(val)
                              for val in value]
            if status == ADDED:
                output.append(ADDED_MESSAGE.format(path,
                                                   key,
                                                   adjusted_value[0]))
            if status == REMOVED:
                output.append(REMOVED_MESSAGE.format(path, key))
            if status == CHANGED:
                output.append(CHANGED_MESSAGE.format(path, key,
                                                     adjusted_value[0],
                                                     adjusted_value[1]))
    iter_str(diff, '')
    return '\n'.join(output)
