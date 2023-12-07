#!/usr/bin/python3
"""
Prime Game Module
"""


def primes(n):
    """
    Return a list of prime numbers between 1 and n inclusive.

    Args:
        n (int): Upper boundary of the range. The lower boundary is always 1.

    Returns:
        list: List of prime numbers.
    """
    prime = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            prime.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return prime


def isWinner(x, nums):
    """
    Determine the winner of the Prime Game.

    Args:
        x (int): Number of rounds of the game.
        nums (list): List of upper limits of the range for each round.

    Returns:
        str or None: Name of the winner or None if the winner cannot be found.
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None

    Maria = Ben = 0

    # Iterate through each round
    for i in range(x):
        # Generate a list of prime numbers up to the given limit
        prime = primes(nums[i])

        # Check if the number of primes is even or odd and update the scores
        if len(prime) % 2 == 0:
            Ben += 1
        else:
            Maria += 1

    # Determine the overall winner based on the scores
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
