limitNumber = 1000
results = 0

for i in range(1, limitNumber):
    if i % 3 == 0 or i % 5 == 0:
        results = results + i
print(f"results = {results}")
