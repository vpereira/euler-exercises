palindromes = []
limitNumber = 999
startNumber = 100


for i in range(startNumber, limitNumber):
    for j in range(startNumber, limitNumber):
        number = i * j
        if str(number) == str(number)[::-1]:
            palindromes.append(number)

print(f"Highest Palindrome: {sorted(palindromes)[-1]}")
