"""
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?
"""

import numpy as np

numberToFactor = 600851475143
# numberToFactor = 13195


def factors(n):
    _factors = []

    # Handle even numbers using NumPy
    while n % 2 == 0:
        _factors.append(2)
        n = n // 2  # Integer division flooring the result

    # Handle odd numbers using NumPy arrays
    potential_factors = np.arange(3, int(np.sqrt(n)) + 1, 2)
    for i in potential_factors:
        while n % i == 0:
            _factors.append(i)
            n = n // i
            # Update potential_factors as n decreases
            if i > np.sqrt(n):
                break

    if n > 2:
        _factors.append(int(n))  # Append the remaining prime factor

    return np.sort(_factors)


print(factors(numberToFactor)[-1])  # Output: 6857
