## Beginner Series #3 Sum of Numbers

# Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.

def get_sum(a,b):
    if a > b:
        a, b = b, a
    sum = a
    while a < b:
        sum += a+1
        a += 1
    return sum
