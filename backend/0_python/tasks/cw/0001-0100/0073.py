## Is this a triangle?

# Implement a function that accepts 3 integer values a, b, c. The function should return true if a triangle can be built with the sides of given length and false in any other case.

def is_triangle(a, b, c): # 4 3 3
    arr = []
    arr.append(a)
    arr.append(b)
    arr.append(c)
    if a==0 or b==0 or c==0:
        return False
    if max(arr) > sum(arr)/2:
        return False
    return (a+b+c)%2 or a==b==c or (max(arr) < sum(arr)/2)
