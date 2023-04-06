#!/usr/bin/python3
'''Method that calculates the fewest number of operations needed to result
in exactly n H characters in the file.
'''

def minOperations(n):
    '''Calculates the fewest number of operations needed to result
    in exactly n H characters.
    '''
    if not isinstance(n, int):
        return 0
    opr_count = 0
    clipboard = 0
    char_count = 1

    while char_count < n:
        if clipboard < char_count:

            clipboard = char_count
            char_count += clipboard
            opr_count += 2

        elif n - char_count > 0 and (n - char_count) % char_count == 0:

            clipboard = char_count
            char_count += clipboard
            opr_count += 2

        elif clipboard > 0:
            char_count += clipboard
            opr_count += 1
    

    return opr_count
