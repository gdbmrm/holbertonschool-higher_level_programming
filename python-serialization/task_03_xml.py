#!/usr/bin/env python3
"""
serialization and deserialization using XML
as an alternative format to JSON.
"""
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):

    racine = ET.Element("<data>")

    for key, value in dictionary.items():
        enfant = ET.SubElement(racine, key)
        enfant.text = str(value)

    tree = ET.ElementTree(racine)
    with open(filename, "wb") as file_to_open:
        tree.write(file_to_open, encoding='unicode')
    
def deserialize_from_xml(filename):

    file_parsed = ET.parse(filename)
    my_dict = {}

    for key, value in file_parsed.items():
        my_dict[key] = value

    return my_dict
