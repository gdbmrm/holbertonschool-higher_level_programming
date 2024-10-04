#!/usr/bin/python3
"""
fonction qui transforme en liste les arguments puis
les integre dans le fichier add_item.json dans un format json
"""
import sys
import os.path
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


if os.path.exists(filename):
    liste = load_from_json_file(filename)
else:
    liste = []

for index in range(1, len(sys.argv)):
    liste.append(sys.argv[index])
save_to_json_file(liste, "add_item.json")
