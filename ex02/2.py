limitNumber = 4000000
fibonacci = [1, 2]

while fibonacci[-1] < limitNumber:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

print(sum([x for x in fibonacci if x % 2 == 0]))
