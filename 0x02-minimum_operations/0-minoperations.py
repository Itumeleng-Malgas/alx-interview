#!/usr/bin/env python3
""" 0. Minimum Operations: Using dynamic programming approach """


def minOperations(n: int) -> int:
    """
    A method that calculates the fewest number of operations needed
    to result in exactly n H characters in the file.
    """

    if n == 1:
        return 0  # It's already an 'H'

    dp = [float('inf')] * (n + 1)

    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0:  # Only consider factors
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n] if dp[n] != float('inf') else 0
