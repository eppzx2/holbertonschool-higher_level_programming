#!/usr/bin/python3
"""
adds all arguments to a python list
"""


import sys
from pathlib import Path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

filename = "add_item.json"


if Path(filename).exists():
    items = load_from_json_file(filename)
else:
    items = []


items.extend(sys.argv[1:])


save_to_json_file(items, filename)
