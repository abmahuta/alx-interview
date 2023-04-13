#!/usr/bin/python3
"""
Module that parses a log and prints stats to stdout
"""
from sys import stdin

status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

size = 0


def parse_line(line):
    """Parses a log line"""
    items = line.split()
    status_code = items[-2]
    if status_code in status_codes:
        status_codes[status_code] += 1
    size = int(items[-1])
    return size


def print_stats():
    """Prints the accumulated logs"""
    print(f"File size: {size}")
    for status, count in sorted(status_codes.items()):
        if count:
            print(f"{status}: {count}")


if __name__ == "__main__":
    count = 0
    try:
        for line in stdin:
            size += parse_line(line)
            count += 1
            if count == 10:
                print_stats()
                count = 0
    except KeyboardInterrupt:
        print_stats()
        raise
    print_stats()

