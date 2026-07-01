#!/usr/bin/python3
"""Reads stdin line by line and computes metrics.

Log format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

Every 10 lines, and on keyboard interruption (CTRL+C), prints:
- Total file size
- Number of lines by status code, in ascending order
"""
import sys
import re

total_size = 0
status_counts = {}
line_count = 0

pattern = re.compile(
    r'^\S+ - \[.*?\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$'
)


def print_stats():
    """Print the total file size and status code counts collected so far."""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        print("{}: {}".format(code, status_counts[code]))


def main():
    """Read stdin line by line, parse log lines, and print stats."""
    global total_size, line_count

    try:
        for line in sys.stdin:
            line = line.strip()
            match = pattern.match(line)
            if match is None:
                continue

            status_code = match.group(1)
            file_size = int(match.group(2))

            total_size += file_size

            if status_code in ["200", "301", "400", "401", "403", "404", "405", "500"]:
                status_counts[status_code] = status_counts.get(status_code, 0) + 1

            line_count += 1

            if line_count % 10 == 0:
                print_stats()

    except KeyboardInterrupt:
        print_stats()
        raise


if __name__ == "__main__":
    main()
