## You're a square!

# You like building blocks. You especially like building blocks that are squares. And what you even like more, is to arrange them into a square of square building blocks! However, sometimes, you can't arrange them into a square. Instead, you end up with an ordinary rectangle! Those blasted things! If you just had a way to know, whether you're currently working in vain… Wait! That's it! You just have to check if your number of building blocks is a perfect square.

from math import sqrt

def is_square(n):    
    if n <= 0:
        return False if n<0 else True
    my_sqrt = sqrt(n)
    return int(my_sqrt) == n/my_sqrt
