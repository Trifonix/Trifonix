## Square Every Digit

# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

def square_digits(num):
    return int("".join(str(int(digit) ** 2) for digit in str(num)))
