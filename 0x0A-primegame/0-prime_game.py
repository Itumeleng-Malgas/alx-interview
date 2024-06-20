#!/usr/bin/python3
"0. Prime Game"


def primes(n):
    """
    Return list of prime numbers between 1 and n inclusive.
    
    Args:
        n (int): Upper boundary of range. Lower boundary is always 1.
    
    Returns:
        list: List of prime numbers up to and including n.
    """
    if n < 2:
        return []
    
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers
    
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    
    return [p for p in range(n + 1) if sieve[p]]


def isWinner(x, nums):
    """
    Determines the winner of the Prime Game.
    
    Args:
        x (int): Number of rounds of the game.
        nums (list): Upper limit of range for each round.
    
    Returns:
        str: Name of the winner ('Maria' or 'Ben') or None if there is no winner.
    """
    if x is None or nums is None or x == 0 or not nums:
        return None
    
    # Count the number of primes up to the maximum number in nums
    max_num = max(nums)
    primes_list = primes(max_num)
    
    # Create a prefix sum array for the number of primes up to each number
    prime_counts = [0] * (max_num + 1)
    for prime in primes_list:
        for i in range(prime, max_num + 1):
            prime_counts[i] += 1
    
    Maria = Ben = 0
    
    for num in nums:
        if prime_counts[num] % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    
    return None
