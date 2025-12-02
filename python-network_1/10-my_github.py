#!/usr/bin/python3
"""
uses the Github API to display your user id.
"""


import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    try:
        response = requests.get(url, auth=(username, password))
        if response.status_code == 200:
            user_data = response.json()
            print(user_data.get('id'))
        else:
            print("None")
    except requests.RequestException:
        print("None")
