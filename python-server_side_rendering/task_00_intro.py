import logging
import os

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

PLACEHOLDERS = ["name", "event_title", "event_date", "event_location"]


def generate_invitations(template, attendees):
    if not isinstance(template, str):
        logging.error("Invalid input: template must be a string.")
        return

    if not isinstance(attendees, list) or not all(
            isinstance(attendee, dict) for attendee in attendees
    ):
        logging.error(
            "Invalid input: attendees must be a list of dictionaries."
        )
        return

    if not template:
        logging.error("Template is empty, no output files generated.")
        return

    if not attendees:
        logging.error("No data provided, no output files generated.")
        return

    for i in range(len(attendees)):
        templat = template
        for placeholder in PLACEHOLDERS:
            value = attendees[i].get(placeholder)
            templat = templat.replace(
                '{' + placeholder + '}',
                str(value) if value else "N/A"
            )

        try:
            with open(f'output_{i + 1}.txt', 'w') as f:
                f.write(templat)
        except IOError as e:
            logging.error(f"Could not write output_{i + 1}.txt: {e}")