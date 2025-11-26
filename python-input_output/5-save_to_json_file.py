#!/usr/bin/python3
"""
we need an import
"""


import json


def save_to_json_file(my_obj, filename):
    """return yazmiriq cunki sayib qaytarar. json dump cevirir jsona"""

    with open(filename, "w", encoding="utf-8") as j:
        json.dump(my_obj, j)
