#!/usr/bin/env python3

import sys
from collections import defaultdict

def print_statistics(total_size, status_counts):
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        count = status_counts[status_code]
        print(f"{status_code}: {count}")

def main():
    total_size = 0
    status_counts = defaultdict(int)
    lines_processed = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            parts = line.split()
            if len(parts) != 9:
                # Skip lines with incorrect format
                continue

            _, _, _, _, _, status_code, file_size = parts

            try:
                status_code = int(status_code)
                file_size = int(file_size)
            except ValueError:
                # Skip lines with non-integer status code or file size
                continue

            total_size += file_size
            status_counts[status_code] += 1
            lines_processed += 1

            if lines_processed % 10 == 0:
                print_statistics(total_size, status_counts)

    except KeyboardInterrupt:
        # If CTRL + C is pressed, print the current statistics
        print_statistics(total_size, status_counts)
        sys.exit(0)

if __name__ == "__main__":
    main()

