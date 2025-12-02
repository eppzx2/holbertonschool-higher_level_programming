#!/usr/bin/python3
"""
fetching an url
""" 


import urllib.request


with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    body =  response.read()

print(f"Body response:\n\t- type: {type(body)}")
print(f"\t- content: {body}")
print(f"\t- utf8 content: {body.decode('utf-8')}")
