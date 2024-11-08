#!/usr/bin/python3
import os
"""
Python function that generates personalized invitation files
from a template with placeholders and a list of objects.
Each output file should be named sequentially, starting from 1.
You will also implement specific error handling for various edge cases.
"""

template = """Hello {name},

You are invited to the {event_title} on {event_date} at {event_location}.

We look forward to your presence.

Best regards,
Event Team"""

attendees = [
    {
        "name": "Alice",
        "email": "alice@example.com",
        "event_title": "Annual Tech Conference",
        "event_date": "December 15, 2024",
        "event_location": "New York City"
    },
    {
        "name": "Bob",
        "email": "bob@example.com",
        "event_title": "Annual Tech Conference",
        "event_date": "December 15, 2024",
        "event_location": "New York City"
    },
    {
        "name": "Charlie",
        "email": "charlie@example.com",
        "event_title": "Annual Tech Conference",
        "event_date": "December 15, 2024",
        "event_location": "New York City"
    },
]


def generate_invitations(template, attendees):
    """
    generate invitations
    """
    if not isinstance(template, str):
        raise TypeError("Template must be a string")
        return

    if not isinstance(attendees, list):
        raise TypeError("Attendees must be a list")
        return

    for dico in attendees:
        if not isinstance(dico, dict):
            raise TypeError("Each value of attendees must be type dict")
            return

    if not template:
        raise ValueError("Template is empty, no output files generated.")
        return

    if not attendees:
        raise ValueError("No data provided, no output files generated.")

    for idx, dico in enumerate(attendees, start=1):
        filename = f"output_{idx}.txt"
        text_changed = template
        for key, value in dico.items():
            if value is None:
                value = "N/A"
            text_changed = text_changed.replace(f"{{{key}}}", value)

        try:
            if not os.path.exists(filename):
                with open(filename, "w") as file:
                    file.write(text_changed)
        except Exception as e:
            print(f"Cannot create/write in {filename}: {e}")
