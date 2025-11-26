#!/usr/bin/python3
"""
importimport
""" 


import sys
import importlib.util
from pathlib import Path


spec = importlib.util.spec_from_file_location(
    "save_to_json_file", "./5-save_to_json_file.py"
)
save_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(save_module)


spec2 = importlib.util.spec_from_file_location(
    "load_from_json_file", "./6-load_from_json_file.py"
)
load_module = importlib.util.module_from_spec(spec2)
spec2.loader.exec_module(load_module)

filename = "add_item.json"
items = []

if Path(filename).is_file():
    items = load_module.load_from_json_file(filename)

items.extend(sys.argv[1:])
save_module.save_to_json_file(items, filename)
