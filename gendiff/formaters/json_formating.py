import json as json_package


def json(diff, sorting=False):
    return json_package.dumps(diff, sort_keys=sorting)
