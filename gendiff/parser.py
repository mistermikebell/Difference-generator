import json

import yaml


def parse(content, extension):
    if extension == 'json':
        return json.load(content)
    return yaml.load(content, Loader=yaml.SafeLoader)