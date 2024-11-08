#!/usr/bin/python3

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

    for dico in attendees:
        if dico is None:
            dico = "N/A"
        template.replace(dico)

    if os.path.exists(output_X) is None:
        with open(output_X.txt, "w") as file:
            file.write(template)

    