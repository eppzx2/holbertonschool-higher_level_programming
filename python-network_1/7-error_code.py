#!/usr/bin/python3
"""
Exception handling in requests package
"""


import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        response = requests.get(url)
        if response.status_code >= 400:
            print(f"Error code: {response.status_code}")
        else:
            print(response.text)
    except requests.RequestException as e:
        print(f"Error: {e}")
