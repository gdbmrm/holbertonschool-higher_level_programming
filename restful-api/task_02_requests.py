#!/usr/bin/python3
import requests

def fetch_and_print_posts():
    response = requests.get()
    print(response.status_code)

    if response.status_code == 200:
        parsed_data = response.json()

    for titles in parsed_data:
        print(titles)

def fetch_and_save_posts():

    response = requests.get()
    if response.status_code == 200:
        parsed_data = response.json()
        
    dict_id = {post["id"]: post for post, values in parsed_data}
    dict_title = {post["title"]: post for post, values in parsed_data}
    dict_body = {post["body"]: post for post, values in parsed_data}

    with open("posts.csv", "w"):
        csv.DictWriter("posts.csv")
