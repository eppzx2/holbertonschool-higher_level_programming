#!/usr/bin/python3
"""
Response header value
"""


import urllib.request
import sys


url = sys.argv[0]
with urllib.request.urlopen(url) as response:
    print(response.headers.get('X-Request-Id'))
