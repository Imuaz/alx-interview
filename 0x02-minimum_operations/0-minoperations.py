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
        return res  # No new operations added
    '''
    can be achieve by factorizing the number and sum up its prime factors
    i = 2
    while i * i <= n:
        while n % i == 0:
            res += i #Add the prime factor i to the result
            n //= i # Divide n by i to reduce it

        i += 1 # Move on to the next potential prime factor

    if n > 1:
        res += n # If n is greater than 1 after the loop, add it to the result
    '''
    i = 2  # Start with the smallest potential divisor, which is 2
    while i <= n:
        while n % i == 0:
            res += i
            n = n // i  # Divide 'n' by 'i' to update it

        i += 1

    return res
