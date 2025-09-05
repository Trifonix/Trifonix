"""
Задача - вы забыли код на своем кодовом замке на чемодане
там 3 цифры от 0 до 9
напишите программу, которая за вас подберёт этот код
"""
comm = '\n#### #### #### #### #### #### #### ####\n'

for x in range(10):
  for y in range(10):
    for z in range(10):
      print(x,y,z)
print(comm)

#### #### #### #### #### #### #### ####

nums = [2,3,5,7]
for x in nums:
  for y in nums:
    for z in nums:
      print(x,y,z)
print(comm)

#### #### #### #### #### #### #### ####

for x in range(10):
  for y in range(10):
    if x*x != y:
      print('(',x,':',y,')', sep='', end=' ')
    else:
      print('     ', sep='', end=' ')
  print()
print(comm)

#### #### #### #### #### #### #### ####

for x in range(10):
  for y in range(10):
    print(f"({x}:{y})", end=' ')
  print()
print(comm)
