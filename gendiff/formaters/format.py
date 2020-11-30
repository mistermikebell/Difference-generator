from gendiff.formaters.json import json
from gendiff.formaters.plain import plain
from gendiff.formaters.stylish import stylish


def choose(formater):
    formaters = {
        'json': json,
        'plain': plain,
        'stylish': stylish
    }
    return formaters[formater]
