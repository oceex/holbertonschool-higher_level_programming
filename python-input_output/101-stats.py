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
import re

total_size = 0
status_counts = {}
line_count = 0

pattern = re.compile(
    r'"GET /projects/260 HTTP/1\.1"\s+(\d{3})\s+(\d+)\s*$'
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
        for
