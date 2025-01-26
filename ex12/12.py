# https://en.wikipedia.org/wiki/Triangular_number

divisorsNum = 500
divisors = 0


def isPrime(n):
    # instead of call math.sqrt we can simply **.5 which does the same but its cheaper
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def calculateTriangleNumber(n):
    return int(n * (n + 1) / 2)


def calculateDivisors(n):
    _divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            _divisors.append(i)
    return len(_divisors)


i = 3000

while divisors < divisorsNum:
    triangleNumber = calculateTriangleNumber(i)
    if not isPrime(triangleNumber):
        divisors = calculateDivisors(triangleNumber)
        print(f"Triangle number: {triangleNumber}, divisors: {divisors}")
    i += 1
