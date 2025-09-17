## Find the odd int

# Given an array of integers, find the one that appears an odd number of times. There will always be only one integer that appears an odd number of times.

def find_it(seq):
    y = {}
    for x in seq:
        if x in y:
            y[x] += 1
        else:
            y[x] = 1
    for x in y:
        if y[x] % 2 != 0:
            return x
