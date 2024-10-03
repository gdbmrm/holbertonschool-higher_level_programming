#!/usr/bin/env python3
"""
The objective of this exercise is to gain experience
in reading data from one format (CSV)
and converting it into another format (JSON)
using serialization techniques.
"""
import csv
import json

def convert_csv_to_json(csv_filename):
    """
    fonction convert csv to json
    """
    try:
        liste = []
        with open(csv_filename, "r") as file_csv:
            file_read = csv.DictReader(file_csv)
            for row in file_read:
                liste.append(row)
        liste_de_liste = json.dumps(liste)
        with open("data.json", "w") as file_data:
            file_data.write(liste_de_liste)
            return True
    except FileNotFoundError:
        return False
