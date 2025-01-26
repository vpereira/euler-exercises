sumOfSquares = 0
numSum = 0
limitNumber = 100
for i in range(1, limitNumber + 1):
    sumOfSquares = sumOfSquares + (i * i)
    numSum = numSum + i

squareOfSums = numSum * numSum

diffBtwSums = squareOfSums - sumOfSquares

print(f"The sum of the Squares is {sumOfSquares}")
print(f"The square of the sum of the squares is {squareOfSums}")
print(f"The diff between the sum of squares and the squares of sum is {diffBtwSums}")
