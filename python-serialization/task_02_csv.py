#!/usr/bin/env python3

import csv
import json

def convert_csv_to_json(csv_filename):

    try:
        liste = []
        with open(csv_filename, "r") as file_csv:
            file_read = csv.reader(file_csv)
            for row in file_read:
                liste.append(csv.DictReader(row))
        with open("data.json", "w+") as file_data:
            liste = json.dumps(liste)
            file_data.write(liste)
            return True
    except FileNotFoundError:
        return False
