#!/usr/bin/env python3
"""
XML serialization
"""


import xml.etree.ElementTree as ET


def _convert_to_str(value):
    return str(value)


def _convert_from_str(value):
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False

    if value.isdigit():
        return int(value)

    try:
        return float(value)
    except ValueError:
        pass

    return value


def serialize_to_xml(dictionary, filename):
    try:
        root = ET.Element("data")

        for key, value in dictionary.items():
            item = ET.SubElement(root, key)
            item.text = _convert_to_str(value)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)

        return True

    except Exception:
        return False


def deserialize_from_xml(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}

        for elem in root:
            result[elem.tag] = _convert_from_str(elem.text)

        return result

    except Exception:
        return None
