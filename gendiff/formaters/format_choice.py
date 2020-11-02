from gendiff.formaters.json_formating import json

from gendiff.formaters.plain import plain

from gendiff.formaters.stylish import stylish


def choose_formater(formater):
    formaters = {
        'json': json,
        'plain': plain,
        'stylish': stylish
    }
    return formaters[formater]