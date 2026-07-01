#!/usr/bin/python3
"""Reads stdin line by line and computes metrics.

Log format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

Every 10 lines, and on keyboard interruption (CTRL+C) or end of input,
prints:
- Total file size
- Number of lines by status code, in ascending order
"""
import sys

VALID_CODES = ["200", "301", "400", "401", "403", "404", "405", "500"]

total_size = 0
status_counts = {}
line_count = 0


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
            parts = line.split()
            if len(parts) < 2:
                continue

            statuscode = parts[-2]
            size_str = parts[-1]

            try:
                file_size = int(size_str)
            except ValueError:
                continue

            total_size += file_size

            if statuscode in VALID_CODES:
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
