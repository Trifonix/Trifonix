## Reversed sequence

# Build a function that returns an array of integers from n to 1 where n>0.

"""
def reverse_seq(n):
    return [num for num in range(n, 0, -1)]
"""

def reverseseq(n):
    return list(range(n, 0, -1))
