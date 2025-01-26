numberToFactor = 600851475143
# numberToFactor = 13195
factors = []

def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for i in range(2, int(numberToFactor/2)):
    if numberToFactor % i == 0 and isPrime(i):
        print(f"Appended {i}")
        factors.append(i)

print(factors[-1])
