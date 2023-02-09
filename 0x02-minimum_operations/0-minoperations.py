#!/usr/bin/python3
'''Minimum Operations '''


def minOperations(n):
    '''
    calculate the fewest number of operations
    needed to result in exactly n H
    '''
    char_count = 1
    h_count = 0
    cnt = 0

    while char_count < n:
        if h_count == 0:
            h_count = char_count
            cnt += 1

        if char_count == 1:
            char_count += h_count
            cnt += 1

        remaining = n - char_count
        if remaining < h_count:
            return 0

        if remaining % char_count != 0:
            char_count += h_count
            cnt += 1
        else:
            h_count = char_count
            cnt += 2

    if char_count == n:
        return cnt
    else:
        return 0

