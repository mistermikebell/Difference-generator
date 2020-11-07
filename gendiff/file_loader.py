import json
import yaml


def load_file(file_path):
    if file_path.endswith('.json'):
        with open(file_path) as file_for_read:
            return json.load(file_for_read)
    with open(file_path) as file_for_read:
        return yaml.load(file_for_read, Loader=yaml.SafeLoader)