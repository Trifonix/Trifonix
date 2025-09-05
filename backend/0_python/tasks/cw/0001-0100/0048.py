## Duplicate Encoder

# The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

def duplicate_encode(word):
    new_str = ""
    word = list(word.lower())
    dicting = {}
    for x in word:
        if x in dicting:
            dicting[x] += 1
        else:
            dicting[x] = 1
    for y in word:
        if dicting[y] > 1:
            new_str += ')'
        else:
            new_str += '('
    return new_str
