#!/usr/bin/python3
import os


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
    }
]

def generate_invitations(template, attendees):

    if not isinstance(template, str):
        raise TypeError ("Template must be a string")
        return

    if not isinstance(attendees, list):
        raise TypeError ("Attendees must be a list")
        return

    for dico in attendees:
        if not isinstance(dico, dict):
            raise TypeError ("Each value of attendees must be type dict")
            return

    if len(template) == 0:
        raise ValueError ("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        raise ValueError ("No data provided, no output files generated.")

    text_changed = template

    for dico in attendees:
        for key,value in dico.items():
            if value is None:
                value = "N/A"
            text_changed = text_changed.replace(f"{{{key}}}", value)

    print(text_changed)

    try:
        if not os.path.exists("output_X"):
            with open("output_X.txt", "w+") as file:
                file.write(text_changed)
    except Exception as e:
        print("Cannot create/write in file")

