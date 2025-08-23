## List Filtering

# In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

def filter_list(l):
    new_arr = []
    for item in l:
        if isinstance(item, int) and item >= 0:
            new_arr.append(item)
    return new_arr
