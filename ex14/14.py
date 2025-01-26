def generate_even(n):
    return int(n / 2)


def generate_odd(n):
    return int(3 * n + 1)


def is_even(n):
    return n % 2 == 0


currentNumber = 0
longestChain = {"startNumber": 0, "chain": 0}

while currentNumber < 1000000:
    currentNumber += 1
    startNumber = currentNumber
    chain = 1
    while startNumber != 1:
        if is_even(startNumber):
            startNumber = generate_even(startNumber)
        else:
            startNumber = generate_odd(startNumber)
        chain += 1
    print(f"Start number: {currentNumber}, chain = {chain}")
    if chain > longestChain["chain"]:
        longestChain["startNumber"] = currentNumber
        longestChain["chain"] = chain

print(
    f"Start number: {longestChain['startNumber']}, chain = {longestChain['chain']}"
)  # 837799
