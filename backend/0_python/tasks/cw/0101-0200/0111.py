## If you can't sleep, just count sheep!!

# Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.

"""
def count_sheep(n):
    sheep_str = ""
    x = 1
    for i in range(n, 0, -1):
        sheep_str += str(x) + " sheep..."
        x += 1
    return sheep_str
"""

def count_sheep(n):
    return ''.join(f"{i} sheep..." for i in range(1,n+1))
