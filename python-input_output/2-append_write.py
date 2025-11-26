#!/usr/bin/python3
"""
a is adding at the end of line not overwrites
"""


def append_write(filename="", text=""):
    """return func is for return number of symbols after u.write function"""

    with open(filename, "a", encoding="utf-8") as u:
        return u.write(text)
