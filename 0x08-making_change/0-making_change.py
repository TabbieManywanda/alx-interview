#!/usr/bin/python3

'''Change comes from within'''

from typing import List


def makeChange(coins: List[int], total: int) -> int:
    '''Return: fewest number of coins needed to meet `total`'''

    if total <= 0:
        return 0

    if coins is None or len(coins) == 0:
        return -1

    num = 0
    sorted_coins = sorted(coins, reverse=True)
    balance = total

    for coin in sorted_coins:
        while (balance % coin >= 0 and balance >= coin):
            num += int(balance / coin)
            balance = balance % coin

    num = num if balance == 0 else -1

    return num
