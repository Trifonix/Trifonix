## Beginner - Reduce but Grow

# Given a non-empty array of integers, return the result of multiplying the values together in order.

def grow(arr):
    res = 1
    for num in arr:
        res *= num
    return res
