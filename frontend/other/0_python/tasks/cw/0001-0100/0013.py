## Sum of positive

# You get an array of numbers, return the sum of all of the positives ones.

def positive_sum(arr):
    total = 0
    for number in arr:
        if number > 0:
            total += number
    return total
