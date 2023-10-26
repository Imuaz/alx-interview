#!/usr/bin/python3
'''
UTF-8 Validation Module
'''


def validUTF8(data):
    '''
    determines if a given data set represents a valid UTF-8 encoding
    '''
    count = 0  # stores the number of following bytes
    mapping = {0: 0, 2: 1, 3: 2, 4: 3}  # num of consecutive 1s to the f-bytes

    for num in data:
        if count == 0:
            # get the num of consecutive 1s in the first four bits
            count = mapping.get(num >> 4 if num >> 5 == 0b110 else num >> 3, -1)
            if count == -1:  # not a valid UTF-8
                return False
        else:  # if count is !=0 check the following bytes
            if num >> 6 != 0b10:  # if byte doesn't start with 10 not UTF-8
                return False

        count -= 1  # decrement count by 1 after checking each byte
        # if count != 0 at the end, there are missing bytes and its invalid
        if count != 0:
            return False
        return True  # it is valid
