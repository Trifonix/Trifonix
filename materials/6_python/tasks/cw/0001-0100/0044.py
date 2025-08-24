## Sum of two lowest positive integers

# Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.

def sum_two_smallest_numbers(numbers):
    lowest_first = min(numbers)
    numbers.remove(lowest_first)
    lowest_second = min(numbers)
    return lowest_second + lowest_first
