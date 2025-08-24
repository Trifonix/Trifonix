## Isograms

# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

def is_isogram(string):
    letters = [chr(x) for x in range(ord('a'), ord('{'))]
    string = string.lower()
    for x in string:
        if x not in letters:
            return False
        else:
            letters.remove(x)
    return True
