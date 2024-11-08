#!/usr/bin/python3
"""
Python function that generates personalized invitation files
from a template with placeholders and a list of objects.
Each output file should be named sequentially, starting from 1.
You will also implement specific error handling for various edge cases.
"""
import os


def generate_invitations(template, attendees):
    """
    generate invitations
    """
    if not isinstance(template, str):
        raise TypeError("Template must be a string")

    if not isinstance(attendees, list):
        raise TypeError("Attendees must be a list")

    for dico in attendees:
        if not isinstance(dico, dict):
            raise TypeError("Each value of attendees must be type dict")

    if not template:
        raise ValueError("Template is empty, no output files generated.")

    if not attendees:
        raise ValueError("No data provided, no output files generated.")

    for idx, dico in enumerate(attendees, start=1):
        filename = f"output_{idx}.txt"
        text_changed = template
        text_changed = text_changed.replace(
            "{name}", str(dico.get("name", "name:N/A")))
        text_changed = text_changed.replace(
            "{event_title}", str(dico.get("event_title", "event_title:N/A")))
        text_changed = text_changed.replace(
            "{event_date}", str(dico.get("event_date", "event_date:N/A")))
        text_changed = text_changed.replace(
            "{event_location}", str(dico.get(
                "event_location", "event_location:N/A")))

        try:
            with open(filename, "w") as file:
                file.write(text_changed)
                print(f"Generated {file.name}")
        except Exception as e:
            print(f"Cannot create/write in {filename}: {e}")
