#!/usr/bin/python3
import sys
import signal

# Define the status codes to track
status_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}

# Initialize variables to store statistics
line_count = 0
total_file_size = 0
status_code_counts = {code: 0 for code in status_codes}

def print_statistics():
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes, key=int):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")

def process_line(line):
    global line_count, total_file_size, status_code_counts
    
    # Split the line into components
    parts = line.split()
    
    if len(parts) != 7:
        return  # Skip lines with incorrect format
    
    ip, date, request, status_code, file_size = parts
    
    if not status_code.isdigit() or status_code not in status_codes:
        return  # Skip lines with invalid status code
    
    line_count += 1
    total_file_size += int(file_size)
    status_code_counts[status_code] += 1

    # Print statistics after every 10 lines
    if line_count % 10 == 0:
        print_statistics()

def signal_handler(sig, frame):
    print_statistics()

# Register the signal handler for CTRL+C
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line = line.strip()
        process_line(line)
except KeyboardInterrupt:
    pass

# Print final statistics
print_statistics()

