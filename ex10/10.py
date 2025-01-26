limitNumber = 2000000
primes = [2]


def isPrime(n):
    # instead of call math.sqrt we can simply **.5 which does the same but its cheaper
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


for currentNumber in range(3, limitNumber + 1, 2):
    if isPrime(currentNumber):
        primes.append(currentNumber)
    print(f"currentNumber {currentNumber}")
    print(f"primes len = {len(primes)}")

print(f"The sum of the  primes under {limitNumber} is {sum(primes)}")
