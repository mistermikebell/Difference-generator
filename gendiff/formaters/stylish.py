from gendiff.statuses import CHANGED_STATUS, SIGNS

def stylish(diff):
    def iter_str(node, output, level):
        for key, info in node.items():
            if info['status'] == CHANGED_STATUS:
                for v in info['value']:
                    output += iter_str({key: v}, '', level)
            elif isinstance(info['value'], dict):
                after_bracket = '   ' * level + '  }'
                new_output = '{\n' + iter_str(info['value'], '', level + 1) + after_bracket
                sign = SIGNS[info['status']]
                key = '   ' * level + sign + ' ' + key
                output += '{}: {}\n'.format(key, new_output)
            else:
                sign = SIGNS[info['status']]
                key = '   ' * level + sign + ' ' + key
                output += '{}: {}\n'.format(key, info['value'])
        return output
    return '{\n' + iter_str(diff, '', 1) + '}'