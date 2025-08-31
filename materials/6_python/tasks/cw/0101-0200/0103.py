## Ones and Zeros

# Given an array of ones and zeroes, convert the equivalent binary value to an integer. Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

"""
def binary_array_to_number(arr):
    string = ''
    for num in arr:
        string += str(num)
    string = string[::-1]
    number = 0
    i = 0
    for let in string:
        if int(let) == 1:
            number += 2**i
        i += 1
    return number
"""

def binary_array_to_number(arr):
    return int("".join(map(str, arr)), 2)
