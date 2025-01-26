"""
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

palindromes = []
limitNumber = 999
startNumber = 100


for i in range(startNumber, limitNumber):
    for j in range(startNumber, limitNumber):
        number = i * j
        if str(number) == str(number)[::-1]:
            palindromes.append(number)

print(f"Highest Palindrome: {sorted(palindromes)[-1]}")
