## Unique In Order

# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

def unique_in_order(sequence):
    if not sequence:
        return []
    temp = sequence[0]
    arr = []
    for x in sequence:
        if x != temp:
            arr.append(temp)
            temp = x
    arr.append(temp)
    return arr
