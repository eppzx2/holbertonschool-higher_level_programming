#!/usr/bin/python3
import urllib.request
with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    body =  response.read()

print(f"Body response:\n\t- {body.decode('utf-8')}")

