#!/usr/bin/python3
"""
Consuming and processing data from an API using Python
"""
import requests
import csv


def fetch_and_print_posts():
    """
    function fetch and print posts
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status code: {}".format(response.status_code))

    if response.status_code == 200:
        for item in response:
            print(item['title'])


def fetch_and_save_posts():
    """
    fetch and save posts
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        data = response.json()

        with open("posts.csv", "w", newline='') as file_to_write:
            file_writer = csv.DictWriter(
                file_to_write, fieldnames=['id', 'title', 'body'])
            file_writer.writeheader()
            for element in data:
                writer.writerow([element['id'], element['title'],
                                 element['body']])
