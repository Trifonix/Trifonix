def count_divisors(n):
  k = 0
  for i in range(1, n+1):
    if divisible(n, i):
      k += 1
  return k

def divisible(n, i):
  return n % i == 0

for i in range(1, 100):
  if count_divisors(i) == 2:
    print(i)
