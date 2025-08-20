def f(*args):
  return max([x for x in args if x % 2 == 0])

print(f(10, 20, 31))

# **kwargs