for a in range(0, 500):
  for b in range(0, 500):
    for c in range(0, 500):
      if a > b or c < b:
        continue
      if a + b + c == 1000:
        if (a ** 2) + (b ** 2) == (c ** 2):
          print(f"a = {a}, b = {b} and c = {c}")
          print(f"Product is {a * b * c}")
          break

