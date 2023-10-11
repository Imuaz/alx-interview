#!/usr/bin/env python3
'''
Module for the minimum operation
'''


def minOperations(n: int) -> int:
    '''
    Calculate the minimum number of operations to achieve `n` 'H' characters
    in the file.
    '''
    if n <= 1 or type(n) is not int:
        return 0

    dp = [float('inf')] * (n + 1)
    dp[1] = 0

    for i in range(2, n + 1):
        for d in range(2, i + 1):
            if i % d == 0:
                dp[i] = min(dp[i], dp[d] + i // d)

    return dp[n]
