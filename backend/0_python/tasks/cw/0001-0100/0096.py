## Find Maximum and Minimum Values of a List

# Your task is to make two functions ( max and min, or maximum and minimum, etc., depending on the language ) that receive a list of integers as input, and return the largest and lowest number in that list, respectively. Each function returns one number.

def minimum(list):
    minimum = list[0]
    for i in range(1, len(list)):
        if list[i] < minimum:
            minimum = list[i]
    return minimum

def maximum(list):
    maximum = list[0]
    for i in range(1, len(list)):
        if list[i] > maximum:
            maximum = list[i]
    return maximum
