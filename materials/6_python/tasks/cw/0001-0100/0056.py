## Convert string to camel case

# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

def to_camel_case(text):
    string = ""
    big = False
    for x in text:
        if ord(x.lower()) in range(ord("a"), ord('{')):
            if big:
                string += x.upper()
                big = False
            else:
                string += x
        else:
            big = True
    return string
