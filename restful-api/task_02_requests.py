#!/usr/bin/python3
"""
Consuming and processing data from an API using Python
"""
import requests
import json
import csv


def fetch_and_print_posts():
    """
    function fetch and print posts
    """
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    print("Status code: {}".format(response.status_code))

    if response.status_code == 200:
        parsed_data = response.json()

    for titles in parsed_data:
        print(parsed_data[titles])

def fetch_and_save_posts():
    """
    fetch and save posts
    """
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    if response.status_code == 200:
        data = response.json()

    my_list = [
        {'id': data['id'], 'title': data['title'],
            'body': data['body']} for post in data]

    with open("posts.csv", "w", newline='') as file_to_write:
        file_writer = csv.DictWriter(
            file_to_write, fieldnames=['id', 'title', 'body'])
        
        file_writer.writeheader()
        file_writer.writerows(my_list)
