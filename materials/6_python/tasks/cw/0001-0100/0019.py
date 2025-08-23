## Square(n) Sum

# Complete the square sum function so that it squares each number passed into it and then sums the results together.

def square_sum(numbers):
    if not numbers:
        return 0
    else:
        square_nums = [n * n for n in numbers]
        square_sum_nums = sum(square_nums)
        return square_sum_nums
