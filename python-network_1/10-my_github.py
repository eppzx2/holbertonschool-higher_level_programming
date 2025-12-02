#!/usr/bin/python3
"""
It sends a GET request to GitHub's /user API endpoint,
using Basic Authentication (username and token)
"""


import requests
import sys

#eger if name falan yazmasaag index error verir
if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

url = "https://api.github.com/user"

response = requests.get(url, auth=(username, token))

if response.status_code == 200:
    user_data = response.json()
    print(user_data['id'])
else:
    print(f"Failed to retrieve user information. HTTP Status Code: {response.status_code}")
