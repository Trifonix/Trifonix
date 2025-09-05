## Reverse words

# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

def reverse_words(text):
    return " ".join([s[::-1] for s in text.split(' ')])
