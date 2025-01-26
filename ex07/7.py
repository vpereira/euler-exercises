primes = [2]

element = 10001

counter = 1


def isPrime(n):
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


while len(primes) <= element:
    counter = counter + 1
    if isPrime(counter):
        primes.append(counter)

print(f"element: {primes[element-1]}")
