## Does my number look big in this?

# A Narcissistic Number (or Armstrong Number) is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).

def narcissistic( value ):
    res = 0
    length = len(str(value))
    for x in str(value):
        res += int(x)**length
    return res==value
