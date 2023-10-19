#!/usr/bin/python3
'''
Log parsing module
'''
import sys
import signal


sts_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}

line_count = 0
total_file_size = 0
sts_code_counts = {code: 0 for code in sts_codes}

def print_statistics():
    print(f'File size: {total_code_counts}')
    for code in sorted(sts_codes, key=int):
        if sts_code_counts[code] > 0:
            print(f'{code}: {sts_code_counts[code]}')

def process_line(line):
    global line_count, total_file_size, sts_code_counts

    parts = line.split()

    if len(parts) != 7:
        return

    ip, date, request, sts_code, file_size = parts

    if not sts_code.isdigit() or sts_code not in sts_codes:
        return

    line_count += 1
    total_file_size += int(file_size)
    sts_code_counts[sts_code] += 1

    if line_count % 10 == 0:
        print_statistics()

def signal_handler(sig, frame):
    print_statistics()

signal.signal(signal.SIGINT, signal_handler)


try:
    for line in sys.stdin:
        line  = line.strip()
        process_line(line)
except KeyboardInterrupt:
    pass

print_statistics()
