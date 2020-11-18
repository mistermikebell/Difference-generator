import json

import yaml


def load_file(file_path):
    with open(file_path) as file_for_read:
        if file_path.endswith('.json'):
            return json.load(file_for_read)
        return yaml.load(file_for_read, Loader=yaml.SafeLoader)
