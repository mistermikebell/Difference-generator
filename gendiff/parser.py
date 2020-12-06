import json

import yaml


def parse(content, extension):
    if extension == 'json':
        return json.loads(content)
    elif extension == 'yaml' or extension == 'yml':
        return yaml.safe_load(content)
    else:
        raise Exception('ExtensionError: Only JSON or YAML are allowed')
