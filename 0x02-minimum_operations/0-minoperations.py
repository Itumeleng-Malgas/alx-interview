#!/usr/bin/python3
""" Minimum Operations: Using dynamic programming approach """

def minOperations(n):
    """
    We initialize a DP table dp with size n + 1, where dp[i] represents the
    minimum number of operations to achieve i characters.
    """

    if n == 1:
        return 0  # It's already an 'H'

    dp = [float('inf')] * (n + 1)  # Initialize DP array
    dp[1] = 0  # Base case

    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0:  # Only consider factors
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n] if dp[n] != float('inf') else 0
