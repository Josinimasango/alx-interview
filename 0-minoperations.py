#!/usr/bin/python3
"""
method that calculates the fewest number of operations needed
"""


def minOperations(n):
    """
    Calculating the fewest number of operations needed.

    Args:
        n (int): number of H characters.

    Returns:
        int: number of operations needed.
        If n is impossible to achieve, return 0.
    """
    c = 1  # Characters in file
    cb = 0  # Clipboard contents
    op = 0  # Operations count

    # Iterate until the desired number
    while c < n:
        # If clipboard is empty, copy all characters
        if cb == 0:
            cb = c
            op += 1

        # If no characters have been pasted yet, paste clipboard contents
        if c == 1:
            c += cb
            op += 1
            continue

        rem = n - c  # Remaining characters to paste

        # Check if it's impossible to achieve n characters
        if rem < cb:
            return 0

        # If remaining characters cannot be evenly divided, paste clipboard
        if rem % c != 0:
            c += cb
            op += 1
    
        # copy all and then paste
        else:
            cb = c
            c += cb
            op += 2

    # Check if desired result is achieved
    if c == n:
        return op
    else:
        return 0
