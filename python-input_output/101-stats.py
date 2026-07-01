#!/usr/bin/python3
"""Reads stdin line by line and computes metrics.

Every 10 lines, and on keyboard interruption (CTRL+C) or end of input,
prints:
- Total file size
- Number of lines by status code, in ascending order
"""
import sys
import re

total_size = 0
status_counts = {}
line_count = 0

pattern = re.compile(
    r'"GET /projects/260 HTTP/1\.1"\s+(\d{3})\s+(\d+)\s*$'
)


def print_stats():
    """Print the total file size and status codexy."""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        print("{}: {}".format(code, status_counts[code]))


def main():
    """Read stdin line by line, parse log lines, and print stats."""
    global total_size, line_count

    try:
        for line in sys.stdin:
            match = pattern.search(line)
            if match is None:
                continue

            statuscode = match.group(1)
            file_size = int(match.group(2))

            total_size += file_size
            x = ["200", "301", "400", "401", "403", "404", "405", "500"]
            if statuscode in x:
                status_counts[statuscode] = status_counts.get(statuscode, 0)+1

            line_count += 1

            if line_count % 10 == 0:
                print_stats()

    except KeyboardInterrupt:
        print_stats()
        raise
    else:
        print_stats()


if __name__ == "__main__":
    main()
