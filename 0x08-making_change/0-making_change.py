#!/usr/bin/python3
"""
Making Change: 0. Change comes from within
"""


def makeChange(coins, total):
    """Return the minimum number of coins needed to meet a given total.
    """

    if total <= 0:
        return 0
    if not coins:
        return -1

    coins.sort(reverse=True)
    coin_count = 0

    for coin in coins:
        if total >= coin:
            count = total // coin
            coin_count += count
            total -= count * coin
        if total == 0:
            return coin_count

    return -1 if total > 0 else coin_count
