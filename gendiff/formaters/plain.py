from gendiff.statuses import *


def plain(diff):
    def iter_str(node, output, path):
        for key, info in node.items():
            if info['status'] == NO_CHANGE_STATUS and isinstance(info['value'], dict):
                new_output = iter_str(info['value'], '', path + key + '.')
                output += new_output
                path = ''
            if info['status'] in [ADDED_STATUS, DELETED_STATUS]:
                if isinstance(info['value'], dict):
                    val = '[complex value]'
                else:
                    val = "'{}'".format(str(info['value']))
                if info['status'] == ADDED_STATUS:
                    output += "Property '{}{}' was added with value: {}\n".format(path, key, val)
                else:
                    output += "Property '{}{}' was removed\n".format(path, key)
            if info['status'] == CHANGED_STATUS:
                val = ['[complex value]' if isinstance(val, dict) else "'{}'".format(str(info['value'])) for val in info['value']]
                output += "Property '{}{}' was updated. From {} to {}\n".format(path, key, val[0], val[1])
        return output
    return iter_str(diff, '', '')