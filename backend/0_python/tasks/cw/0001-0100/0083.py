## Sum of odd numbers

# Given the triangle of consecutive odd numbers. Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.

def row_sum_odd_numbers(n):
    temp = -1
    summ = 0
    for x in range(1, n+1):
        print('xxxx xxxx')
        for y in range(x):
            temp += 2
            if x==n:
                summ += temp
    return summ
