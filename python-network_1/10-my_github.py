#!/usr/bin/python3
"""
github credentials login
"""


import sys
import requests


def get_github_user_id(username, token):
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, token))
    
    if response.status_code == 200:
        data = response.json()
        print(data['id'])
    else:
        print("Error:", response.status_code)

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    
    get_github_user_id(username, token)
