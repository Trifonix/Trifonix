import sys

x = [10, 20, 30]  # 2
y = x             # 3

print(sys.getrefcount(x))

x[0] = 8          # 3
y = 4             # 2

print(sys.getrefcount(x))

x = [10]          # [10, 20, 30] : 0 | 42 : 2

print(sys.getrefcount(x))
