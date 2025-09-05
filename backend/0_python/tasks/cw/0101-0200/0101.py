## Find the unique number

# There is an array with some numbers. All numbers are equal except for one. Try to find it!

def find_uniq(arr):
    array = list(set(arr))
    num1, num2 = array[0], array[1]
    dicting = {}
    dicting[num1] = 0
    dicting[num2] = 0
    for x in arr:
        if num1 == x:
            dicting[num1] += 1
        elif num2 == x:
            dicting[num2] += 1
        if dicting[num1] > 1:
            return num2
        elif dicting[num2] > 1:
            return num1

"""
def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b
"""
