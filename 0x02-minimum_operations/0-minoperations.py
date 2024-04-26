#!/usr/bin/python3
"""
Given a number n, write a method that calculates the fewest number
of operations needed to result in exactly n H characters in the file.
"""


def minOperations(n: int) -> int:
    """
    Calculates the fewest number of operations
    needed to result in exactly n H characters
    in the file.

    Args:
    - n (int): The target number of H characters.

    Returns:
    - int: The fewest number of operations.
    """
    process = 2
    op = 0
    while n > 1:
        while n % process == 0:
            op += process
            n /= process
        process += 1
    return op

