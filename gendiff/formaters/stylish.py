from gendiff.constants import CHANGED, REMOVED, ADDED, SIGNS, NO_CHANGE, INDENT


def stylish(diff, sorting=False):
    output = []

    def iter_str(node, level):
        if sorting:
            node = dict(sorted(node.items()))
        for key, info in node.items():
            indent = INDENT * level
            if isinstance(info, tuple):
                status = info[0]
                sign = SIGNS[info[0]]
                value = info[1]
            else:
                status = NO_CHANGE
                sign = SIGNS[NO_CHANGE]
                value = info
            if status == CHANGED:
                iter_str({key: (REMOVED, value[0])}, level)
                iter_str({key: (ADDED, value[1])}, level)
            elif isinstance(value, dict):
                key = "".join([indent, sign, ' ', key, ': {'])
                output.append(key)
                iter_str(value, level + 1)
                output.append(indent + '  }')
            else:
                key = "".join([indent, sign, ' ', key])
                output.append('{}: {}'.format(key, value))
    iter_str(diff, 1)
    return '{\n' + '\n'.join(output) + '\n}'
