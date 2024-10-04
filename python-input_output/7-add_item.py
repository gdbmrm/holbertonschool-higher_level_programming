#!/usr/bin/python3
"""
fonction qui transforme en liste les arguments puis
les integre dans le fichier add_item.json dans un format json
"""
import sys
import os
import json

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"

if os.path.exists(filename):
    liste = load_from_json_file(filename)
else:
    liste = []

liste.extend(sys.argv[1:])
save_to_json_file(liste, filename)
