## Disemvowel Trolls

# Your task is to write a function that takes a string and return a new string with all vowels removed.

def disemvowel(string_):
    string_new = ''
    for l in string_:
        if l.lower() not in ['a','e','i','o','u']:
            string_new += l
    return string_new
