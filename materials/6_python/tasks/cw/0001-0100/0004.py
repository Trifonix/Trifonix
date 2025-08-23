## Vowel Count

# Return the number (count) of vowels in the given string. We will consider a, e, i, o, u as vowels for this Kata (but not y).

def get_count(sentence):
    count = 0
    for x in sentence:
        if x in ['a','e','i','o','u']:
            count += 1
    return count
