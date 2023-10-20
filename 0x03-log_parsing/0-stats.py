#!/usr/bin/python3
'''Log parsing Module '''
import sys
sts_codes_dict = {'200': 0, '301': 0, '400': 0, '401': 0,
                  '403': 0, '404': 0, '405': 0, '500': 0}
total_file_size = 0
line_counts = 0


def input_statistic(total_file_size):
    '''prints input statistics'''
    print(f'File size: {total_file_size}')
    for key, value in sorted(sts_codes_dict.items()):
        if value != 0:
            print(f'{key}: {value}')


try:
    for line in sys.stdin:
        # spliting the stdin line by whide space
        line_read = line.split(' ')

        # checking if the splited list of string length is more than 4
        if len(line_read) > 4:
            status_code = line_read[-2]  # extract the status code
            file_size = int(line_read[-1])  # extract the file size
            if status_code in sts_codes_dict.keys():
                sts_codes_dict[status_code] += 1
            total_file_size += file_size
            line_counts += 1
        if line_counts == 10:
            line_counts = 0
            input_statistic(total_file_size)
except Exception as ex:
    pass
finally:
    input_statistic(total_file_size)
