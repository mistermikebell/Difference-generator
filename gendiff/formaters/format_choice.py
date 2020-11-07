from gendiff.formaters.json_formating import json
from gendiff.formaters.plain import plain
from gendiff.formaters.stylish import stylish
from gendiff.constants import JSON, PLAIN, STYLISH


def choose_formater(formater):
    formaters = {
        JSON: json,
        PLAIN: plain,
        STYLISH: stylish
    }
    return formaters[formater]
