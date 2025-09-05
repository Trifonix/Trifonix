## Bit Counting

# Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

def count_bits(n):
    return sum([int(x) for x in bin(n)[2:]])
