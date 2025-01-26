"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

limitNumber = 2000000
primes = [2]


def isPrime(n):
    # instead of call math.sqrt we can simply **.5 which does the same but its cheaper
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


for currentNumber in range(3, limitNumber + 1, 2):
    if isPrime(currentNumber):
        primes.append(currentNumber)

print(f"The sum of the  primes under {limitNumber} is {sum(primes)}")  # 142913828922
