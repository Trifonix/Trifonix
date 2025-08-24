## Counting Duplicates

# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

def duplicate_count(text):
    dicting = {}
    counter = 0
    for x in [x.lower() for x in list(text)]:
        if x in dicting:
            dicting[x] += 1
        else:
            dicting[x] = 1
    for y in dicting:
        if dicting[y] > 1:
            counter += 1
    return counter
