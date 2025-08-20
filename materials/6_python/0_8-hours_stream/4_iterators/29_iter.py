# a = [x**2 for x in range(10000000000)] MemoryError

a = [x**2 for x in range(100)]

print(a)

b = (x**2 for x in range(101101101))

print(b)

for x in b:
  print(x)
  if x > 100:
    break

for y in b:
  print(y)
