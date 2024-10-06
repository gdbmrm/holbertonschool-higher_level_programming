#!/usr/bin/python3
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
        enfant = ET.Element(key)
        enfant.text = str(value)
        racine.append(enfant)

    tree = ET.ElementTree(racine)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    deserialize from xml
    """
    tree = ET.parse(filename)
    racine = tree.getroot()

    my_dict = {}

    for child in racine:
        my_dict[child.tag] = child.text

    return my_dict
