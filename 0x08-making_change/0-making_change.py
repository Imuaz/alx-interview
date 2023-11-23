#!/usr/bin/python3
'''
Coin change Module
'''


def makeChange(coins, total):
    '''
    determine the fewest number of coins needed to meet a given amount total
    '''
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]
