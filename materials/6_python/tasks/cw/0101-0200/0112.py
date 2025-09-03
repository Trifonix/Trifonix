## Equal Sides Of An Array

# You are going to be given an array of integers. Your job is to take that array and find an index N where the sum of the integers to the left of N is equal to the sum of the integers to the right of N. If there is no index that would make this happen, return -1.

"""
def find_even_index(arr):
    for x in range(0, len(arr)):
        left = sum(arr[0:x])
        right = sum(arr[x+1:])
        if left == right:
            return x
    return -1
"""

def find_even_index(arr):
    r = [i for i in range(len(arr)) if sum(arr[0:i]) == sum(arr[i+1:])]
    return r[0] if r else -1
