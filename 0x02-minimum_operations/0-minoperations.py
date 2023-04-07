#!/usr/bin/python3
'''Method that calculates the fewest number of operations needed to result
in exactly n H characters in the file.
'''

def minOperations(n):
    '''Calculates the fewest number of operations needed to result
    in exactly n H characters.
    '''
def minOperations(n):
    if n == 1:
        return 0
    ops = 0
    i = 2
    while i <= n:
        if n % i == 0:
            ops += i
            n //= i
        else:
            i += 1
    return ops

