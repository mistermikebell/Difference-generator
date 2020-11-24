from gendiff.formaters.json_formating import json
from gendiff.formaters.plain import plain
from gendiff.formaters.stylish import stylish

JSON = 'json'
PLAIN = 'plain'
STYLISH = 'stylish'


def choose(formater):
    formaters = {
        JSON: json,
        PLAIN: plain,
        STYLISH: stylish
    }
    return formaters[formater]
