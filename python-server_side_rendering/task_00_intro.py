import os.path


def generate_invitations(template, attendees):
    if isinstance(template, str) and isinstance(attendees, list):
        for attendee in attendees:
            if not isinstance(attendee, dict):
                raise TypeError('attendees list must have a dictionaries')
    else:
        raise TypeError('template must be a string and attendees must be a list')
    if not template:
        raise TypeError('Template is empty, no output files generated.')
    if not attendees:
        raise TypeError('No data provided, no output files generated')
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

