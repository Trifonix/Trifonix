import random

for x in dir(random):
  print(x)

a = ['cat', 'dog', 'bird', 'bread']
print("\n==== ====", random.choice(a))
