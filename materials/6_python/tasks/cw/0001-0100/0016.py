## Highest and Lowest

# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

def high_and_low(numbers):
    hal = [int(x) for x in numbers.split()]
    return f'{max(hal)} {min(hal)}'
