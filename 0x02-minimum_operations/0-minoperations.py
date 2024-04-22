#!/usr/bin/env python3
""" 0. Minimum Operations: Using dynamic programming approach """


def minOperations(n):
    """
    We initialize a DP table dp with size n + 1, where dp[i] represents the
    minimum number of operations to achieve i characters.

    We iterate over each length i from 2 to n. For each length i, we try all
    possible divisors j. If j evenly divides i, we update dp[i] with the
    minimum of its current value and the number of operations required to
    achieve j characters plus the number of pasting operations required to reach
    i characters.

    We also consider the case where i // j is a divisor of i, in which case we
    update dp[i] with the minimum of its current value and the number of operations
    required to achieve i // j characters plus the number of pasting operations
    required to reach i characters.
"""

    if n == 1:
        return 0

    dp = [float('inf')] * (n + 1)  # Initialize DP table
    dp[1] = 0  # Base case

    for i in range(2, n + 1):
        j = 1
        while j * j <= i:
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)
                dp[i] = min(dp[i], dp[i // j] + j)
            j += 1

    return dp[n]
