## Exes and Ohs

# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

def xo(s):
    count_x = 0
    count_y = 0
    s = s.lower()
    for x in s:
        if x in ['x', 'o']:
            if x == 'x':
                count_x += 1
            else:
                count_y += 1
    return count_x == count_y
