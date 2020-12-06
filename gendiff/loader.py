import re

from gendiff.parser import parse


def get_file_data(file_path):
    with open(file_path) as content:
        extension = re.search('\.(\S+)$', file_path)
        if not extension:
            raise Exception('ExtensionError: Could not recognize'
                            ' file extension')
        return parse(content.read(), extension.group(1))
