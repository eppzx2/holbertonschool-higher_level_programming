#!/usr/bin/python3
"""
json representasiyasi ucun bize import qadagasi qoyulmayib ona gore de import edek
"""


import json


def to_json_string(my_obj):
    """json.dumps python obyektini json stringe cevirir"""

    return json.dumps(my_obj)
