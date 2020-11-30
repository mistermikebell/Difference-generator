from gendiff.diff_tree import (REMOVED, ADDED, CHANGED, UNCHANGED, NESTED)

SIGNS = {REMOVED: '-',
         ADDED: '+',
         CHANGED: ' ',
         NESTED: ' ',
         UNCHANGED: ' '}


def stringify(item):
    if isinstance(item, bool):
        return str(item).lower()
    if item is None:
        return 'null'
    return item


def stylish(diff):
    output = []

    def iter(tree, indent):
        for key in tree.keys():
            if isinstance(tree[key], tuple):
                status, value = tree[key]
                sign = SIGNS[status]
            else:
                status = UNCHANGED
                sign = SIGNS[UNCHANGED]
                value = tree[key]
            if status == CHANGED:
                iter({key: (REMOVED, value[0])}, indent)
                iter({key: (ADDED, value[1])}, indent)
            elif isinstance(value, dict):
                row = '{}{} {}: {{'.format(indent, sign, key)
                output.append(row)
                iter(value, indent + '    ')
                output.append(indent + '  }')
            else:
                output.append('{}{} {}: {}'.format(indent, sign,
                                                   key, stringify(value)))
    iter(diff, '  ')
    return '{\n' + '\n'.join(output) + '\n}'
