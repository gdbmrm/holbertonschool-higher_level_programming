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
        print(titles)


def fetch_and_save_posts():
    """
    fetch and save posts
    """
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    if response.status_code == 200:
        parsed_data = response.json()

    dict_id = [
        {"id": parsed_data["id"]}
        for cle, valeur in parsed_data.items() if "id" in parsed_data]

    dict_title = [
        {"title": parsed_data["title"]}
        for cle, valeur in parsed_data.items() if "title" in parsed_data]

    dict_body = [
        {"body": parsed_data["body"]}
        for cle, valeur in parsed_data.items() if "body" in parsed_data]

    with open("posts.csv", "w+") as file_to_write:
        file_writer = csv.DictWriter(
            file_to_write, fieldnames=["id", "title", "body"])
