#!/usr/bin/python3

'''calculates the fewest number of operations
needed to result in exactly n H characters in the file'''


def minOperations(n):
    '''calculates the fewest number of operations needed
    to result in exactly n H characters in the file'''
    num = 0
    count = 2
    while n > 1:
        while n % count == 0:
            num += count
            n /= count
        count += 1
    return num
