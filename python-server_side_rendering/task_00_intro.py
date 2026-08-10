import logging
import os

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

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

    try:
        for i in range(len(attendees)):
            templat = template
            for attendee in attendees[i]:
                if attendees[i][attendee]:
                    templat = templat.replace('{'+attendee+'}', attendees[i][attendee])
                else:
                    templat = templat.replace('{'+attendee+'}', f"{attendee}: N/A")

            with open(f'output_{i+1}.txt', 'w') as f:
                f.write(templat)
    except Exception as e:
        raise e

