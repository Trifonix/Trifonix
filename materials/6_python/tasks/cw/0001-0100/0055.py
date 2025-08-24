## Persistent Bugger

# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

def persistence(n):
    n = [int(x) for x in list(str(n))]
    res = 1
    count = 0
    while len(n)>1:
        res = 1
        for x in n:
            res *= x
        n = [x for x in [int(x) for x in list(str(res))]]
        count += 1
    return count
