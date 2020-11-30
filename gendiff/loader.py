import json

import yaml


def parse(content, extension):
    if extension == 'json':
        return json.loads(content)
    return yaml.safe_load(content)


def get_file_data(file_path):
    with open(file_path) as content:
        if file_path.endswith('.json'):
            return parse(content.read(), 'json')
        return parse(content.read(), 'yaml')
