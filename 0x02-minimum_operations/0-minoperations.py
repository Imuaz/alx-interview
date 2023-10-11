#!/usr/bin/env python3
'''
Module for the minimum operation
'''


def minOperations(n):
    '''
    Calculate the minimum number of operations to achieve `n` 'H' characters
    in the file.
    '''
    res = 0

    if n <= 1 or type(n) is not int:
        return res

    i = 2
    while i <= n:
        while n % i == 0:
            res += i
            n = n // i

        i += 1

    return res
