#!/usr/bin/python3
'''
UTF-8 Validation Module
'''


def validUTF8(data):
    '''
    determines if a given data set represents a valid UTF-8 encoding
    '''
    cont_bytes = 0

    for byte in data:
        # if the current byte is a valid cont. byte.
        if cont_bytes > 0:
            if (byte & 0xC0) != 0x80:
                return False
            cont_bytes -= 1
        else:
            # Determine the no. of continuation bytes based on the leading bits
            if (byte & 0x80) == 0:
                cont_bytes = 0
            elif (byte & 0xE0) == 0xC0:
                cont_bytes = 1
            elif (byte & 0xF0) == 0xE0:
                cont_bytes = 2
            elif (byte & 0xF8) == 0xF0:
                cont_bytes = 3
            else:
                return False

    # If we expect more continuation bytes, the data is incomplete.
    return cont_bytes == 0
