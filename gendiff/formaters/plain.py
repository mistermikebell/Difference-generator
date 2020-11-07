from gendiff.constants import NO_CHANGE, CHANGED, ADDED, REMOVED


def plain(diff, sorting=False):
    output = []

    def iter_str(node, path):
        if sorting:
            node = dict(sorted(node.items()))
        for key, info in node.items():
            if info[0] == NO_CHANGE and isinstance(info[1], dict):
                iter_str(info[1], path + key + '.')
                path = ''
            if isinstance(info[1], list):
                value = info[1]
            else:
                value = [info[1]]
            adjusted_value = ['[complex value]'
                              if isinstance(val, dict)
                              else "'{}'".format(val)
                              for val in value]
            if info[0] == ADDED:
                output_string = "".join(["Property '",
                                         path, key,
                                         "' was added with value: ",
                                         adjusted_value[0]])
                output.append(output_string)
            if info[0] == REMOVED:
                output_string = "".join(["Property ", path, key,
                                         " was removed"])
                output.append(output_string)
            if info[0] == CHANGED:
                output_string = "".join(["Property '", path, key,
                                         "' was updated. From ",
                                         adjusted_value[0], " to ",
                                         adjusted_value[1]])
                output.append(output_string)
    iter_str(diff, '')
    return '\n'.join(output)
