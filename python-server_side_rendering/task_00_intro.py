#!/usr/bin/python3
"""
templating program
"""


import os


def generate_invitations(template, attendees):
    """
    some documentation
    """

    if not isinstance(template, str):
        print("Error: Template should be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees should be a list of dictionaries.")
        return

    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    for i, attendee in enumerate(attendees, start=1):

        processed = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            if value is None or value == "":
                value = "N/A"
            processed = processed.replace(f"{{{key}}}", str(value))

        filename = f"output_{i}.txt"

        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(processed)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
            continue
