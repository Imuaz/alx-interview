#!/usr/bin/python3
'''
Minimum operations module
'''


def minOperations(n: int) -> int:
    """
    Calculate the minimum number of operations to achieve `n` 'H' characters
    in the file.
    """
    res = 0

    if n <= 1 or type(n) is not int:
        return res

    i = 2
    while i * i <= n:
        while n % i == 0:
            res += i
            n //= i

        i += 1

    if n > 1:
        res += n

    return res
