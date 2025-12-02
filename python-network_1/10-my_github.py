#!/usr/bin/python3


import requests


username = "eppzx2"
token = "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"

url = "https://api.github.com/user"

response = requests.get(url, auth=(username, token))

if response.status_code == 200:
    user_data = response.json()
    print(user_data['id'])
else:
    print(f"Failed to retrieve user information. HTTP Status Code: {response.status_code}")
