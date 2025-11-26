#!/usr/bin/python3
"""
w edende overwrite edir, return write funksiyasinin deyerin qaytarir
"""


def write_file(filename="", text=""):
    """nece simvol yazildisa qaytarir"""

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
