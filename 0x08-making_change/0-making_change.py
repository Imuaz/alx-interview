#!/usr/bin/python3
'''
Coin change Module
'''


def makeChange(coins, total):
    """
    Return the minimum number of coins needed to meet a given total
    Args:
        coins (list of ints): a list of coins of different values
        total (int): total value to be met
    Return:
        Number of coins or -1 if meeting the total is not possible
    """
    total_count = 0
    coins.sort(reverse=True)

    if total <= 0:
        return 0
    
    for coin in coins:
        counter = total // coin
        total %= coin
        total_count += counter
        if total == 0:
            return total_count
    
    return -1
