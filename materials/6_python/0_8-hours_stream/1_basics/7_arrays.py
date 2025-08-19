# Списки, Кортежи, Словари, Множества

a = [10, 24, 'a', 'abc']
print(a[0])
print(len(a))
s = 'text'
print(list(s))
a.append(42)
print(a[-1])
b = a.copy()
print('другой объект',b)
print()

"""
sum()
max()
min()
"""

# Кортеж (tuple)
t = (1, 2, 3)
print(t)
print(t.__sizeof__())
print()

# Словарь (dictionary)
d = dict()
d[12] = 100
d['hello'] = 20
for x in d:
  print(x, d[x])

# Множества (set)
p = set()
p.add(7)
p.add(8)
p.add(7)
p.add(9)
print(p)
