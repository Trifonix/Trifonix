## Playing with digits

# Given two positive integers n and p, we want to find a positive integer k, if it exists, such that the sum of the digits of n raised to consecutive powers starting from p is equal to k * n.

"""
def dig_pow(n, p):
    string = str(n)
    sum = 0
    for i in range(len(string)):
        sum += int(string[i]) ** p
        p += 1
    if (sum/n == sum//n):
        return sum // n
    else:
        return -1
"""

def dig_pow(n, p):
  s = 0
  for i,c in enumerate(str(n)):
     print(i, c)
     s += pow(int(c),p+i)
  return s/n if s%n==0 else -1
