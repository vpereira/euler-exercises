"""
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?
"""

numberToFactor = 600851475143
# numberToFactor = 13195


def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False

    return True


def factors(n):
    _factors = []

    # handle even numbers
    while n % 2 == 0:
        _factors.append(2)
        n = n // 2  # integer division flooring the result

    # handle odd numbers
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            _factors.append(i)
            n = n // i

    return sorted(_factors)


print(sorted([i for i in factors(numberToFactor) if isPrime(i)])[-1])  # 6857
