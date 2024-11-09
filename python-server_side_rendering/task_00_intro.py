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
    code
    """
    if not isinstance(template, str):
        print("Error: The template is not a string.")
        return

    if template.strip() == "":
        print("Error: Template is empty, no output files generated.")
        return

    if not isinstance(attendees, list) or not all(
            isinstance(item, dict) for item in attendees
            ):
        print("Error: Attendees must be a list of dictionaries.")
        return

    if len(attendees) == 0:
        print("Error: No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        output_filename = f"output_{index}.txt"

        try:
            message = template
            for placeholder in ["name", "event_title",
                                "event_date", "event_location"]:
                value = attendee.get(placeholder, "N/A") or "N/A"
                message = message.replace(f"{{{placeholder}}}", value)

            with open(output_filename, "w") as output_file:
                output_file.write(message)
                print(f"Invitation saved to {output_filename}")

        except Exception as e:
            print(f"Error: Could not write to file {output_filename}. {e}")
