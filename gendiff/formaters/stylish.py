REMOVED = 'removed'
ADDED = 'added'
NO_CHANGED = 'no_changed'
CHANGED = 'changed'
NESTED = 'nested'
SIGNS = {REMOVED: '-',
         ADDED: '+',
         CHANGED: ' ',
         NESTED: ' ',
         NO_CHANGED: ' '}


def stylish(diff):
    output = []

    def iter_str(tree, indent):
        for key in sorted(tree.keys()):
            indent
            if isinstance(tree[key], tuple):
                status, value = tree[key]
                sign = SIGNS[status]
            else:
                status = NO_CHANGED
                sign = SIGNS[NO_CHANGED]
                value = tree[key]
            if status == CHANGED:
                iter_str({key: (REMOVED, value[0])}, indent)
                iter_str({key: (ADDED, value[1])}, indent)
            elif isinstance(value, dict):
                row = "{}{} {}: {{".format(indent, sign, key)
                output.append(row)
                iter_str(value, indent + '    ')
                output.append(indent + '  }')
            else:
                output.append('{}{} {}: {}'.format(indent, sign, key, value))
    iter_str(diff, '  ')
    return '{\n' + '\n'.join(output) + '\n}'
