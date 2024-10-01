#!/usr/bin/python3
import sys
import os.path
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
"""
fonction qui transforme en liste les arguments puis
les integre dans le fichier add_item.json dans un format json
"""
if os.path.isfile("add_item.json"):
    liste = load_from_json_file("add_item.json")
else:
    liste = []

for index in range(1, len(sys.argv)):
    liste.append(sys.argv[index])
save_to_json_file(liste, "add_item.json")
