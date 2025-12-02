#!/usr/bin/python3
"""
documentation
"""


import requests
import csv


def fetch_and_print_posts():
    """Fetch all posts from JSONPlaceholder and print their titles."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    """Fetch all posts from JSONPlaceholder and save them to a CSV file."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    if response.status_code == 200:
        posts = response.json()
        data_to_save = [
            {'id': post['id'], 'title': post['title'], 'body': post['body']}
            for post in posts
        ]
        
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for item in data_to_save:
                writer.writerow(item)
