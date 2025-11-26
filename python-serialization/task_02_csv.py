#!/usr/bin/env python3
"""
Convert a CSV file into JSON format and save it as data.json
"""


import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert a CSV file into a JSON file"""

    try:
        data_list = []

        with open(csv_filename, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data_list.append(row)

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data_list, json_file, indent=4)
        return True

    except Exception:
        return False
