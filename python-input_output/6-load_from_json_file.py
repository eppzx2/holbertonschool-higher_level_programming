#!/usr/bin/python3
"""
from json we use load but opposite we use dumps
"""


import json


def load_from_json_file(filename):
    """loading"""

    with open(filename, "r") as bob:
        return json.load(bob)
