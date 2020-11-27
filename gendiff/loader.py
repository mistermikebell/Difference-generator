def load_file(file_path):
    with open(file_path) as content:
        if file_path.endswith('.json'):
            return content.read(), 'json'
        return content.read(), 'yaml'
