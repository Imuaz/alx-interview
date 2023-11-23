#!/usr/bin/python3
"""
Coin change Module
"""


def makeChange(coins, total):
    """
    Return the minimum number of coins needed to meet a given total
    Args:
        coins (list of ints): a list of coins of different values
        total (int): total value to be met
    Return:
        Number of coins or -1 if meeting the total is not possible
    """
    if total <= 0:
        return 0
    if coins is None or coins == []:
        return -1

    """Initialize an array to store the minimum number of coins needed for
    each amount from 0 to total"""
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through each coin value
    for coin in coins:
        # Update the dp array for each amount from the coin value to the total
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    """If the value at dp[total] is still infinity, it means the total
    cannot be met"""
    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]
