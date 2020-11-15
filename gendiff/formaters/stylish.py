REMOVED = 'removed'
ADDED = 'added'
NO_CHANGED = 'no_changed'
CHANGED = 'changed'
NESTED = 'nested'
INDENT = '   '
SIGNS = {REMOVED: '-',
         ADDED: '+',
         CHANGED: ' ',
         NESTED: ' ',
         NO_CHANGED: ' '}


def stylish(diff):
    output = []

    def iter_str(tree, level):
        for key in sorted(tree.keys()):
            indent = INDENT * level
            if isinstance(tree[key], tuple):
                status, value = tree[key]
                sign = SIGNS[status]
            else:
                status = NO_CHANGED
                sign = SIGNS[NO_CHANGED]
                value = tree[key]
            if status == CHANGED:
                iter_str({key: (REMOVED, value[0])}, level)
                iter_str({key: (ADDED, value[1])}, level)
            elif isinstance(value, dict):
                row = "{}{} {}: {{".format(indent, sign, key)
                output.append(row)
                iter_str(value, level + 1)
                output.append(indent + '  }')
            else:
                output.append('{}{} {}: {}'.format(indent, sign, key, value))
    iter_str(diff, 1)
    return '{\n' + '\n'.join(output) + '\n}'
