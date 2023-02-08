#!/usr/bin/python3
'''Minimum Operations '''


def minOperations(n):
    '''
    calculate the fewest number of operations
    needed to result in exactly n H
    '''
    char_count = 1 #number of chars in file
    H_count = 0 #number of H copied
    cnt = 0 #operation count

    while char_count < n:
        if H_count == 0:
            H_count = char_count
            cnt += 1

        if char_count == 1:
            char_count += H_count
            cnt += 1
            continue

        remaining = n - char_count
        if remaining < H_count:
            return 0

        if remaining % char_count != 0:
            char_count += H_count
            cnt += 1

        else:
            H_count = char_count
            char_count += H_count
            cnt += 2

    if char_count == n:
        return cnt
    else:
        return 0
        