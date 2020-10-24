
import json

import yaml


def load_file(file_path):
    if file_path.endswith('json'):
        return json.load(open(file_path))
    return yaml.load(open(file_path), Loader=yaml.FullLoader)
