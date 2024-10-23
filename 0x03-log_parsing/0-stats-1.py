#!/usr/bin/python3
import sys
import signal

# Dictionary to store the number of occurrences of each status code
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
total_file_size = 0
line_count = 0

def print_stats():
    """Prints the accumulated metrics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def signal_handler(sig, frame):
    """Handles the CTRL+C signal to print stats."""
    print_stats()
    sys.exit(0)

# Register the signal handler for CTRL+C (KeyboardInterrupt)
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        try:
            # Split and extract relevant fields from the line
            parts = line.split()
            if len(parts) < 7:
                continue
            
            # File size is the last element
            file_size = int(parts[-1])
            total_file_size += file_size

            # Status code is the second-to-last element
            status_code = int(parts[-2])
            if status_code in status_codes:
                status_codes[status_code] += 1
            
            line_count += 1

            # Print stats after every 10 lines
            if line_count % 10 == 0:
                print_stats()

        except (ValueError, IndexError):
            # Skip lines with incorrect format
            continue

except KeyboardInterrupt:
    print_stats()
    raise
