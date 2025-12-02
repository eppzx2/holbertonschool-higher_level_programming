#!/usr/bin/python3
""" Response header value """


import urllib.request
import sys


url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    x_req_id = response.getheader('X-Request-Id')
print(x_req_id)
