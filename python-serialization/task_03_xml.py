#!/usr/bin/env python3
"""
serialization and deserialization using XML
as an alternative format to JSON.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    serialize to xml
    """

    racine = ET.Element("data")

    for key, value in dictionary.items():
        enfant = ET.Element(racine, key)
        enfant.text = str(value)
        racine.append(enfant)

    tree = ET.ElementTree(racine)
    with open(filename, "w+") as file_to_open:
        tree.write(file_to_open)


def deserialize_from_xml(filename):
    """
    deserialize from xml
    """

    file_parsed = ET.parse(filename)
    racine = file_parsed.getroot()

    my_dict = {}
    for enfant in racine:
        my_dict[enfant.tag] = enfant.text

    return my_dict
