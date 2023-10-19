#!/usr/bin/python3
''' module for log parsing '''

import re
import sys

total = 0
counter = 0
sc_dict = {'200': 0, '301': 0, '400': 0, '401': 0,
           '403': 0, '404': 0, '405': 0, '500': 0}

# Regular expression to match the input format
input_format = re.compile(r'^[0-9.]+ - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)\s*$')

def print_data(total):
    ''' function to print statistics for input '''
    print('File size:', total)
    for key, value in sorted(sc_dict.items()):
        if value != 0:
            print('{}: {}'.format(key, value))


try:
    for line in sys.stdin:
        # Check if the input line matches the format
        match = input_format.match(line)

        # If the line does not match the format, skip it
        if not match:
            continue

        # Extract the status code and request size from the match
        status_code = int(match.group(1))
        request_size = int(match.group(2))

        # Check for invalid status codes
        if status_code not in sc_dict:
            print('Invalid status code:', status_code)
            continue

        # Update the metrics
        sc_dict[status_code] += 1
        total += request_size
        counter += 1

        # Print the statistics every 10 lines and at the end of the input
        if counter == 10 or sys.stdin.isatty():
            print_data(total)
            counter = 0
except Exception as ex:
    pass
finally:
    print_data(total)
