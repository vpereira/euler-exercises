numberDividedByAll = 0
num = 0
while numberDividedByAll == 0:
    num = num + 1
    allDivisions = []
    for i in range(1, 20):
        allDivisions.append(num % i == 0)
    if all(allDivisions):
        numberDividedByAll = num

print(f"Number is {numberDividedByAll}")
