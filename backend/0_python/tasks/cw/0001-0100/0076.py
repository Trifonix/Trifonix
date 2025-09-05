## Invert values

# Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

def invert(lst):
    newArr = []
    for item in lst:
        newArr.append(-item)
    return newArr
