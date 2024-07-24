#!/usr/bin/python3

""" determining the fewest number of coins 
needed to meet a given amount total"""


def makeChange(coins, total):
    """
    Returns: few number of coins needed to meet total
        if total is 0, return 0
        if total cannot be met by any number of coins we have, return -1
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    change = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if (total == 0):
            return change
    return -1
