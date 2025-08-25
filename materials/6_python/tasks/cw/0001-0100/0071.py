## Moving Zeros To The End

# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

def move_zeros(lst):
    arr = [n for n in lst if n!=0]
    count = len(lst) - len(arr)
    while count>0:
        arr.append(0)
        count -= 1
    return arr
