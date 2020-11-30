import json

import yaml


def parse(content, extension):
    if extension == 'json':
        return json.loads(content)
    return yaml.safe_load(content)