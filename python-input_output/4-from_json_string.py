#!/usr/bin/python3
"""
jsonla bagli emeliyyatlarda import
"""


import json


def from_json_string(my_str):
    """json strdan pythona cevirerken json.loads"""

    return json.loads(my_str)
